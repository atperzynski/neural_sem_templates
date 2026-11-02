# The data folder

Copyright 2026 Adam T. Perzynski. Licensed under the Apache License, Version 2.0 (TEMPLATE_LICENSE.txt).

The data of this project are kept in this folder on the computers of the people who analyse them,
and they are never committed to the repository. Git ignores everything in this folder except this
file, and `tools/check_no_data.py` refuses any commit that would add a data file anywhere in the
project.

Copy the data file named in `hotsem-project.json` into this folder before running `analysis.R`.
When a colleague joins the project, the data file is shared with them by the route the study's
data agreement allows, such as a secure university share, and never through the repository.
