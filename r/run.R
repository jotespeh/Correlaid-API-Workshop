# load required packages
library(plumber)

# read plumber file
r <- plumb("r/todo.R")

# start server
r$run(port = 8000)
