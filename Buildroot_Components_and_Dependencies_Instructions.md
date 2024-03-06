
## Getting Components and Dependencies from Buildroot

Getting a detailed list of components and dependencies from Buildroot involves generating documentation or reports that enumerate the packages, their versions, dependencies, and possibly their licenses. Here are the methods to do this:

### 1. Legal Information

To generate legal documentation, including licenses and a manifest of all packages:

```sh
make legal-info
```

This command generates files in `output/legal-info` directory, including a manifest (`manifest.csv`), license files, and source files. The manifest lists each package, its version, and its license.

### 2. Graph Dependencies

For generating a graph of package dependencies, ensure Graphviz is installed, then run:

```sh
make graph-depends
```

This produces a `.dot` file in `output/graphs`. Convert it to an image with Graphviz, for example:

```sh
dot -Tpng output/graphs/package-dependencies.dot -o dependencies.png
```

### 3. Package List

To get a list of configured packages and their versions:

```sh
make list-packages
```

To save this list to a file:

```sh
make list-packages > packages_list.txt
```

### 4. Saving Configurations

Ensure to save your Buildroot configuration for future reference or sharing:

```sh
make savedefconfig
```

or by copying the `.config` file manually.

---

These steps provide methods for extracting comprehensive information about the components and dependencies in your Buildroot build. For more details, consult Buildroot's documentation.
