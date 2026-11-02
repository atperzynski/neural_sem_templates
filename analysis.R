# Copyright 2026 Adam T. Perzynski. Licensed under the Apache License, Version 2.0 (TEMPLATE_LICENSE.txt).
#
# Reproduce the model of this project in R with lavaan.
#
# Before running this file, copy the data file {{DATA_FILE}} into the data/ folder of this project,
# where Git ignores it, and open the project in RStudio (double-click the .Rproj file) or in
# Positron (File, Open Folder). Then run this whole file. The cleaning steps in clean.R are applied
# first, and the model in model/model.lav is then fitted and compared, parameter by parameter, with
# the numbers HOT-NUX-SEM showed when the project was saved.

if (!requireNamespace("lavaan", quietly = TRUE)) install.packages("lavaan")

data_file <- file.path("data", "{{DATA_FILE}}")
if (!file.exists(data_file)) {
  stop("The data file was not found at ", data_file, ". Copy it into the data/ folder first; ",
       "it is never kept in the repository.", call. = FALSE)
}

# the cleaning recipe, in dplyr; with no steps recorded it leaves the data as they are
source("clean.R")

# the fit and the comparison, run from inside data/ so that the script finds the file by name
owd <- setwd("data")
on.exit(setwd(owd), add = TRUE)
source(file.path("..", "model", "lavaan_check.R"), echo = FALSE, print.eval = TRUE)
