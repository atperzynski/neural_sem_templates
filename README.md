# HOT-NUX-SEM project template

Copyright 2026 Adam T. Perzynski. Licensed under the Apache License, Version 2.0 (TEMPLATE_LICENSE.txt).

This repository is the template from which every HOT-NUX-SEM project repository is made, so that a
model built in the app can be reproduced in R, shared with co-authors and reviewed on GitHub or
GitLab without the data ever entering a repository. HOT-NUX-SEM fills a copy of this template with
the model, the data dictionary, the cleaning recipe and the results when a project is saved or
pushed, and the same files ship inside the app for people who use GitLab or work offline.

## Starting a project from the template

The usual route is to build the model in HOT-NUX-SEM, create an empty repository on GitHub or
GitLab with the link the **Pack** tab offers, and push the project into it from the app, which
writes these files filled with the model. A project folder can also be downloaded from the **Pack**
tab and put on GitHub with GitHub Desktop, and a person who can see this repository can start a
project here with **Use this template**. In either case, the steps for RStudio,
Positron, GitHub Desktop and the command line are in `GETTING_STARTED.md`, and the way a team works
on one model is in `CONTRIBUTING.md`.

## What every project carries

Every project made from this template carries i) a `.gitignore` that keeps the `data/` folder and
the common data formats out of Git, ii) a pre-commit hook in `.githooks/` that refuses a commit
containing a data file, iii) a check on GitHub (`.github/workflows/check.yml`) and on GitLab
(`.gitlab-ci.yml`) that repeats the data check and confirms that the model parses in lavaan, iv) an
R project file for RStudio, and v) issue and pull request templates for proposing a change to the
model and for reporting a problem. The data check itself is `tools/check_no_data.py`, which uses the
Python standard library only.

## The files the app writes

`README.template.md` becomes the project's README, filled with the model's name, the data file and
the fit, and `analysis.R` names the project's data file. The app also writes `data-dict.yaml`,
`clean.R`, `cleaning.recipe.json`, `hotsem-project.json` and the contents of `model/` and
`results/`, and none of those files holds a row of data.

## Licence

The files of this template are Copyright 2026 Adam T. Perzynski and licensed under the Apache
License, Version 2.0, whose text is in `TEMPLATE_LICENSE.txt`, so that researchers may reuse them in
their own repositories, including public ones. The licence covers the template's files only, and
the model, results and other files a researcher adds belong to that researcher.
