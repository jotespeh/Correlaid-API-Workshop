Plumbing APIs with R: Plumber
========================================================
author: Jan Dix
date: 
autosize: true
css: presi.css

About Plumber
========================================================

### Features:
- Automatically creates documentation
- Only R

### Cons:
- Documentation
- Implementation

Let's code 1
========================================================

- Create an R Project
- Create two files:
  - router.R
  - run.R


```r
dependencies <- c("plumber",    # api package
                  "DBI",        # database interface
                  "RMySQL")     # database driver
install.packages(dependencies)
```

 
Let's code 2
========================================================


```r
# router.R

#* Hello world
#* @get /hello-world
function() {
  return("Hello world.")
}
```


```r
# run.R

# load required packages
library(plumber)

# read plumber file
r <- plumb("r/todo.R")

# start server
r$run(port = 8000)
```


Let's code 3
========================================================



```r
# router.R

#* Add two numbers
#* @param x x-value
#* @param y y-value
#* @get /sum
function(x, y) {
  return(as.numeric(x) + as.numeric(y))
}

#* Get square root of a number
#* @get /sqrt/<x>
function(x) {
  return(sqrt(x))
}
```


Postman
========================================================



Where do I get my data from? Database!
========================================================




```
  id        title                                           comment
1 11    Ein Gruss                                    Noch ein Gruße
2 12 API Workship                      Slides wären echt mal fällig
3 13   Bugs fixen Wer frei von Fehlern ist, werfe den ersten und so
4 14 Note to self                                    Geh mal pennen
5 15 Note to self                                    Geh mal pennen
6 16 Note to self                                    Geh mal pennen
7 17    Ernsthaft                                  Geh jetzt pennen
  date_added
1 2019-11-30
2 2019-11-30
3 2019-11-30
4 2019-11-30
5 2019-11-30
6 2019-11-30
7 2019-11-30
```

Connect to the database
========================================================


```r
# load packages
library(DBI)
library(RMySQL)

# define credentials
host <- "mysql01.manitu.net"
user <- "u38837"
password: <- "<PASSWORD>"
database: <- "db38837"

# connect to the database
connection <- dbConnect(MySQL(),
                        user = user,
                        password = password,
                        dbname = database,
                        host = host)

# get data from database
query <- "SELECT * FROM todo_items;"
response <- dbGetQuery(connection, query)

# disconnect from the database
dbDisconnect(connection)
```


SQL Injections
========================================================

### Don't do:


```r
injectionEnabled <- function (i) {
  return(paste("SELECT * FROM todo_items WHERE id =", i))
}

sql <- injectionEnbaled(";DELETE FROM todo_items;")
```

### Please use:


```r
sql <- "SELECT * FROM todo_items WHERE id = ?id;"
query <- sqlInterpolate(conn, sql, id = id)
```

- [W3School: Introduction to SQL Injection](https://www.w3schools.com/sql/sql_injection.asp)
- [RStudio: SQL injection prevention in R](https://shiny.rstudio.com/articles/sql-injections.html)

GET (Read)
========================================================


```sql
SELECT * FROM todo_items WHERE id = 1;
```
  
POST (Create)
========================================================


```sql
INSERT INTO todo_items (title, comment) VALUES ('New ToDo', 'This is a todo.');
```

PUT (Update)
========================================================


```sql
UPDATE todo_items SET title = 'Old Todo', comment = 'This is an old todo.' WHERE id = 1;
```

DELETE (Delete)
========================================================


```sql
DELETE FROM todo_items WHERE id = 1;
```

What is missing?
========================================================

- Authorization & Authentication
- Proper error handling
- Logging
- Auto-reload in development

Additional links
========================================================

- [Plumber Docs (Jeff Allen)](https://www.rplumber.io/docs/index.html) 
- ["R can API and So Can You!" - Series (Heather Nolis & Jacqueline Nolis)](https://medium.com/tmobile-tech/r-can-api-c184951a24a3)
- [Automatically reload API during development (Jan Dix)](https://medium.com/@dix.jan/automatically-reload-your-plumber-api-during-development-daa7d1f2f41f)

