
# FOSSA CLI Integration Script for Conan

This script integrates FOSSA, an open-source software management and compliance tool, with the Conan package manager. It generates a `fossa-deps.yml` file from your project's Conan dependency graph, which FOSSA can then use to analyze the dependencies for licensing and vulnerability issues.

## How It Works

1. **Data Classes for Dependencies**: The script defines data classes to represent different types of dependencies (`FossaVendorDep`, `FossaCustomDep`, `FossaCustomDepMetadata`) and the final `FossaDep` that includes both vendored and custom dependencies.

2. **Parsing Conan Dependency Graph**: It uses the `conan graph info` command to retrieve the project's dependency graph in JSON format. The script then parses this graph to extract relevant information about each dependency, such as its name, version, license, homepage, and description.

3. **Generating `fossa-deps.yml`**: Based on the gathered information, the script generates a `fossa-deps.yml` file, which includes sections for both vendored dependencies (those with available source code) and custom dependencies (those without available source code on disk).

4. **Logging**: The script uses Python's logging module to log its operations, which can help in troubleshooting if there are issues with the generation process.

## How to Use It

1. **Pre-requisites**: Ensure you have Python 3 and Conan v2 installed on your system. You also need to have the FOSSA CLI installed and configured for your project.

2. **Running the Script**: Place the script in the same directory as your `conanfile.txt`. Run the script using Python 3:

    ```bash
    python3 make_fossa_deps_conan.py
    ```

    You can pass additional arguments to the script that are valid for the `conan graph info` command, except for `--format`, as the script requires the output in JSON format.

3. **FOSSA Analysis**: After generating the `fossa-deps.yml` file, run `fossa analyze` in the directory containing the file to analyze your dependencies with FOSSA.

4. **Troubleshooting and Support**: If you encounter issues, the script provides links to FOSSA support and documentation for further assistance.

## Conclusion

This script automates the process of generating a dependency file for FOSSA analysis from a Conan-based project, making it easier to integrate FOSSA into your software compliance and security workflow.
