# Working on this model together

Proprietary. All rights reserved. Licence to be determined by the inventors.

This project is kept in Git so that every change to the model, the data dictionary or the cleaning
recipe is recorded with its reason and reviewed by a co-author before it is accepted. The practice
below suits a team of a few analysts working on one study, and it applies equally on GitHub and on
GitLab.

## One change, one branch

Each change to the model is made on a branch of its own and proposed as a pull request (a merge
request on GitLab), so that the change, its reason and the fit before and after can be read
together. The *Propose a change to the model* issue template is the place to raise a change before
anyone makes it, and the pull request template asks for the checks a reviewer will look for.

## Making the change in the app

The model is changed in HOT-NUX-SEM rather than by editing the files by hand, because the app fits
the model, checks that it is identified, and writes the model, the lavaan script, the dictionary
and the results together. After the change is made in the app, the project folder is saved over
the local copy, or pushed from the app, and the changed files are committed on the branch. A hand edit to `model/model.lav` is possible, and the project is then opened again in
the app so that the other files are written from the edited model.

## What a reviewer checks

A reviewer reads the reason for the change against the theory and the item content, and against
the book's rules where they apply. The reviewer then confirms that i) no data file is in the pull
request and the data check passed, ii) the model parses, iii) `analysis.R` was run on a computer
holding the data and lavaan agreed with the app, and iv) the wording in `results/` reports fit
against the stated cut-offs and makes no causal claim.

## Sharing the data

The data are shared between the people on the study by the route the study's data agreement
allows, such as a secure university share, and never through Git. The fingerprint in
`hotsem-project.json` lets each analyst confirm that the file in their `data/` folder is the one
the model was fitted to.
