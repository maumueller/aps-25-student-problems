# akeyboardofalltime

This directory contains the files for our competitive programming problem,
"akeyboardofalltime". It is structured following the
[Kattis Problem Package Format, `legacy` version](https://www.kattis.com/problem-package-format/spec/legacy.html).

## Generators

The [`generators`](./generators) directory contains scripts designed to generate
the test cases for the `data` directory. They are designed to be compatible with
[BAPCtools](https://github.com/RagnarGrootKoerkamp/BAPCtools). The generators
are used with the `bt generate` command, and rely on the `networkx` Python
package being available in the Python interpreter used by BAPCtools.
