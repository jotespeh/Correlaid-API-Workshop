# load required packages
library(DBI)

# load database functions
source("r/db.R")

#* List all todo items
#* @get /todo/list
function(){
  conn <- db_connect()
  query <- "SELECT * FROM todo_items;"
  response <- dbGetQuery(conn, query)
  dbDisconnect(conn)
  return(response)
}

#* Get a single todo item by id
#* @get /todo/<id>
function(id) {
  conn <- db_connect()
  sql <- "SELECT * FROM todo_items WHERE id = ?id;"
  query <- sqlInterpolate(conn, sql, id = id)
  response <- dbGetQuery(conn, query)
  dbDisconnect(conn)
  return(response)
}

#* Create a new todo item
#* @post /todo
function(title = NULL, comment = NULL) {
  if (is.null(title)) return("Title is missing.")
  if (is.null(comment)) return("Comment is missing.")
  conn <- db_connect()
  sql <- "INSERT INTO todo_items (title, comment) VALUES (?title, ?comment);"
  query <- sqlInterpolate(conn, sql, title = title, comment = comment)
  response <- dbGetQuery(conn, query)
  dbDisconnect(conn)
  return(response)
}

#* Update a single todo item
#* @put /todo/<id>
function(id, title = NULL, comment = NULL) {
  if (is.null(title) & is.null(comment)) return("Title and comment is missing.")
  conn <- db_connect()
  if (!is.null(title) & !is.null(comment)) {
    sql <- "UPDATE todo_items SET title = ?title, comment = ?comment WHERE id = ?id"
    query <- sqlInterpolate(conn, sql, title = title, comment = comment, id = id)
  }
  if (!is.null(title) & is.null(comment)) {
    sql <- "UPDATE todo_items SET title = ?title WHERE id = ?id"
    query <- sqlInterpolate(conn, sql, title = title, id = id)
  }
  if (is.null(title) & !is.null(comment)) {
    sql <- "UPDATE todo_items SET comment = ?comment WHERE id = ?id"
    query <- sqlInterpolate(conn, sql, comment = comment, id = id)
  }
  response <- dbGetQuery(conn, query)
  sql <- "SELECT * FROM todo_items WHERE id = ?id;"
  query <- sqlInterpolate(conn, sql, id = id)
  response <- dbGetQuery(conn, query)
  dbDisconnect(conn)
  return(response)
}
