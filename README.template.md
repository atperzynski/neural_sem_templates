# {{TITLE}}

Proprietary. All rights reserved. Licence to be determined by the inventors.

This repository holds the structural equation model *{{MODEL_NAME}}*, built in HOT-NUX-SEM on
{{CREATED}} from the data file `{{DATA_FILE}}`, together with its data dictionary, its cleaning
recipe and the scripts that reproduce it in R. The data themselves are never kept here, and a copy
of `{{DATA_FILE}}` is placed in `data/` on each computer that runs the analysis.

## Your data

You are responsible for how you handle your data. Each use of HOT-NUX-SEM with a dataset must
follow the terms under which you hold the data, including any data use agreement, the applicable
privacy laws and regulations, and the requirements of your institutional review board. A public
repository can be read by anyone, so a project whose column names, data dictionary, counts or
results could describe restricted data belongs in a private repository.

## What is in the project

| Path | What it holds |
|---|---|
| `analysis.R` | The script to run. It applies `clean.R` and refits the model with lavaan, comparing every estimate with the app's |
| `clean.R` and `cleaning.recipe.json` | The cleaning steps accepted in the app, as dplyr and as the recipe the app computes from |
| `data-dict.yaml` | What each column is, namely its label, type, levels and missing codes, with no row of data |
| `model/` | The model in lavaan syntax, the lavaan comparison script and the Mplus input, which has not yet been run in Mplus |
| `results/` | The Results section, the Methods paragraph, the parameter and fit tables, and the figure |
| `hotsem-project.json` | The model's name, the version of the app and engine, and the name and fingerprint of the data file |
| `data/` | The data, kept on your computer and ignored by Git |

## Reproducing the analysis

Copy `{{DATA_FILE}}` into `data/`, open the project in RStudio or Positron, and run `analysis.R`.
The fingerprint in `hotsem-project.json` lets you confirm that the file is the one the model was
fitted to, and `GETTING_STARTED.md` describes each step, the Git commands and the data check.

## The model at the time it was saved

{{FIT_LINE}}
