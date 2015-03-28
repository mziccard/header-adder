# Header Adder

Python utility that adds an header to all source files of a given extension nested 
in the provided directory.
Can be used, for instance, to add author information or copyright notice to already existing files.

# Usage

Utility provides the following options:

-   `-h, --help`: shows help message

-   `-i, --input-header=`: path to the file of the header to be added to each source file **\[mandatory\]**

-   `-e, --extension=`: extension of the files to which the header has to be prepended **\[mandatory\]**

-   `-d, --directory=`: target directory  **\[default=./\]**

# Placeholders

Placeholders can be inserted into the template header file that will be translated into the desired data by the Python script:-   `-h, --help`: shows help message

-   `%DATE`: date in ISO format

-   `%FILENAME`: name of the file to which the header is being prepended
