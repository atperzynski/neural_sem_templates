# Getting started with a HOT-NUX-SEM project

Proprietary. All rights reserved. Licence to be determined by the inventors.

This guide takes a project saved from HOT-NUX-SEM to a computer, runs the analysis in R, and shares
the work with co-authors through GitHub or GitLab. Each section stands on its own, so a reader who
already uses Git can go straight to *Running the analysis*. The data of the project never enter the
repository, and the first section explains why and how that rule is kept.

## Why a model is kept in Git

A structural equation model is usually revised many times between the first diagram and the one
that is reported, and a Git repository records every version of the model with its date, its
author and the reason the change was made. Co-authors and reviewers can then follow the path from
the hypothesized model to the reported one, and Ram (2013) and Bryan (2018) describe this
transparency as a benefit of version control for researchers who analyse data. Version control is
also recommended among the basic practices of scientific computing by Wilson and colleagues
(2017), and Blischak, Davenport and Wilson (2016) give a short introduction for researchers who
have not used Git before.

- Blischak JD, Davenport ER, Wilson G. A quick introduction to version control with Git and GitHub.
  PLoS Computational Biology. 2016;12(1):e1004668. doi:10.1371/journal.pcbi.1004668
- Bryan J. Excuse me, do you have a moment to talk about version control? The American
  Statistician. 2018;72(1):20-27. doi:10.1080/00031305.2017.1399928
- Ram K. Git can facilitate greater reproducibility and increased transparency in science. Source
  Code for Biology and Medicine. 2013;8:7. doi:10.1186/1751-0473-8-7
- Wilson G, Bryan J, Cranston K, Kitzes J, Nederbragt L, Teal TK. Good enough practices in
  scientific computing. PLoS Computational Biology. 2017;13(6):e1005510.
  doi:10.1371/journal.pcbi.1005510

## The rule about data

No row of data is ever committed to this repository, whether on GitHub, GitLab or a university
server. The data are kept in the `data/` folder on the computers of the people who analyse them,
and Git ignores that folder. Three checks enforce the rule, namely i) the `.gitignore` file, ii) a
pre-commit hook in `.githooks/` that refuses a commit containing a data file, and iii) a check that
runs on GitHub or GitLab after every push. A download of the project from HOT-NUX-SEM may include
the data for your own use, and the data in such a download stay out of Git all the same.

You are responsible for how you handle your data. Each use of HOT-NUX-SEM with a dataset must
follow the terms under which you hold the data, including any data use agreement, the applicable
privacy laws and regulations, and the requirements of your institutional review board. A
repository made from the link in the app is public unless Private is chosen, and a public
repository can be read by anyone, so a project whose column names, data dictionary, counts or
results could describe restricted data belongs in a private repository.

## Getting the project onto your computer

**If the project is already on GitHub or GitLab**, the simplest route is GitHub Desktop
(https://desktop.github.com), which is free. Choose **File**, then **Clone repository**, pick the
project from the list, and choose a folder on your computer. RStudio and Positron can also clone a
repository, as the next two sections describe, and the command line equivalent is
`git clone <address of the repository>`.

**If the project came as a download from HOT-NUX-SEM**, unzip the folder wherever you keep your
analyses. To put it on GitHub, open GitHub Desktop, choose **File**, then **Add local repository**,
select the folder, and press **Publish repository** with **Keep this code private** ticked.

**Turn on the data check once on each computer.** Open a terminal in the project folder (in RStudio
the **Terminal** tab, in Positron **Terminal**, then **New Terminal**) and run the command below,
after which Git refuses any commit that would add a data file.

```
git config core.hooksPath .githooks
```

## Running the analysis in RStudio

1. Double-click `hot-nux-sem-project.Rproj` (or the `.Rproj` file named after your project), and
   RStudio opens with the project folder as its working directory.
2. Copy the data file named in `hotsem-project.json` into the `data/` folder.
3. Open `analysis.R` and press **Source**. lavaan is installed the first time if it is missing, the
   cleaning steps in `clean.R` are applied, and the model is fitted and compared, parameter by
   parameter, with the numbers HOT-NUX-SEM showed.

To clone a project inside RStudio, choose **File**, then **New Project**, then **Version Control**,
then **Git**, and paste the address of the repository. The **Git** tab of RStudio then shows each
changed file, and **Commit**, **Pull** and **Push** do what their names say.

## Running the analysis in Positron

1. Choose **File**, then **Open Folder**, and select the project folder. Positron starts an R
   session in that folder.
2. Copy the data file named in `hotsem-project.json` into the `data/` folder.
3. Open `analysis.R` and choose **Source R File** from the run menu at the top right of the editor.

The **Source Control** view on the left of Positron lists the changed files, and a commit is made by
writing a message and pressing **Commit**, followed by **Sync Changes** to push and pull. To clone a
project, open the command palette and choose **Git: Clone**.

## Working with the command line

The commands below cover what a HOT-NUX-SEM project needs from Git, and each one is run in a
terminal opened in the project folder.

```
git clone <address>                      # copy the project to this computer
git config core.hooksPath .githooks      # turn on the data check, once per clone
git pull                                 # bring in your co-authors' changes
git switch -c add-sleep-fatigue          # start a branch for one change to the model
git add model data-dict.yaml results     # stage the files HOT-NUX-SEM wrote
git commit -m "Add the sleep and fatigue residual covariance"
git push -u origin add-sleep-fatigue     # share the branch and open a pull request
```

## Bringing a change back from HOT-NUX-SEM

A change to the model is made in HOT-NUX-SEM, where it is fitted and checked, and the app then
writes the project files again. Either save the project folder from the **Pack** tab over the folder on
your computer and commit the files that changed, or push the project from the app into this
repository with one line under **What changed**, which becomes the reason recorded with the new
version. The app writes `model/model.lav`, `model/lavaan_check.R`, `data-dict.yaml`, `clean.R`,
`cleaning.recipe.json` and the files in `results/` together, so they always describe the same
model, and a commit of all of them keeps the history readable.

## Where to get help

A problem with the app is reported with the *Report a problem* issue template of this repository,
which asks for the model and the messages and never for the data. The book that the software follows is Gunzler,
Perzynski and Carle (2021), *Structural Equation Modeling for Health and Medicine*, and the
decision rules quoted in the app carry its page numbers.
