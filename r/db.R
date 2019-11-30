library(DBI)
library(RMySQL)

db_connect <-  function () {
  return(dbConnect(MySQL(),
                   user = Sys.getenv("DB_USER"),
                   password = Sys.getenv("DB_PASSWORD"),
                   dbname = Sys.getenv("DB_NAME"),
                   host = Sys.getenv("DB_HOST")))
}
