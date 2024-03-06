import subprocess
import pandas as pd
import yaml

def run_make_legal_info(buildroot_dir):
    # Run the 'make legal-info' command in the Buildroot directory
    subprocess.run(["make", "legal-info"], cwd=buildroot_dir, check=True, shell=False)

def combine_sources_to_url(csv_path):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_path)

    # Combine 'SOURCE ARCHIVE' and 'SOURCE SITE' into one 'URL' column
    df['URL'] = df.apply(lambda row: row['SOURCE SITE'].rstrip('/') + '/' + row['SOURCE ARCHIVE'] if row['SOURCE SITE'] != 'not saved' else 'not saved', axis=1)

    # Drop the original 'SOURCE ARCHIVE' and 'SOURCE SITE' columns
    df_combined = df.drop(columns=['SOURCE ARCHIVE', 'SOURCE SITE'])
    return df_combined

def convert_to_fossa_yaml(df, yaml_path):
    fossa_deps = {"remote-dependencies": []}
    for _, row in df.iterrows():
        # Extracting the base URL for 'homepage' from the combined URL
        base_url = row['URL'].rsplit('/', 1)[0] if row['URL'] != 'not saved' else 'not available'
        
        dep_entry = {
            "name": row['PACKAGE'],
            "version": row['VERSION'],
            "url": row['URL'],
            "metadata": {
                "description": "",  # Placeholder as the original CSV does not contain descriptions
                "homepage": base_url
            }
        }
        fossa_deps["remote-dependencies"].append(dep_entry)

    # Write to YAML file
    with open(yaml_path, 'w') as file:
        yaml.dump(fossa_deps, file, sort_keys=False, default_flow_style=False, width=float("inf"))

# Paths
buildroot_dir = '/home/ubuntu/buildroot/'  # Buildroot directory path
csv_path = '/home/ubuntu/buildroot/output/legal-info/host-manifest.csv'  # CSV file path
yaml_path = '/home/ubuntu/buildroot/output/legal-info/fossa-deps.yml'  # YAML save path

# Run 'make legal-info' command
run_make_legal_info(buildroot_dir)

# Process CSV and convert to YAML
df_combined = combine_sources_to_url(csv_path)
convert_to_fossa_yaml(df_combined, yaml_path)

print(f"FOSSA dependencies file saved to {yaml_path}")
