
import psycopg2
from datetime import datetime

DBNAME = 'news'


def news_query(query):
    """Connects with news database and runs select queries"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return(results)


def popular_articles():
    """popular_articles will search newsdata.sql and return a list of articles
        in descending order from highest to lowest views."""
    title = 'The most popular articles in order'
    query1 = (" select articles.title, count(*) as num from articles, log "
              "where log.path like concat('%', articles.slug, '%') "
              "group by articles.title "
              "order by num desc")
    run_query = news_query(query1)
    print("    " + title)
    for i in range(len(run_query)):
        print(' {}: Article: {}, Total Views: {}'
              .format(i+1, run_query[i][0], run_query[i][1]))


def popular_authors():
    """popular_authors will search newsdata.sql and return a list of authors
        in descending order from highest to lowest views."""
    title = 'The most popular authors in order'
    query2 = ("select authors.name, sum(top_articles.num) as views "
              "from authors, articles, "
              "(select articles.title, count(*) as num from articles, "
              "log where log.path like concat('%', articles.slug, '%') "
              "group by articles.title order by num desc) as top_articles "
              "where top_articles.title = articles.title and articles.author "
              "= authors.id "
              "group by authors.name order by views desc")
    run_query = news_query(query2)
    print("    " + title)
    for i in range(len(run_query)):
        print(' {}: Author: {}, Total Views: {}'
              .format(i+1, run_query[i][0], run_query[i][1]))


def log_errors():
    "log_errors searches newsdata.sql for any day with log errors "
    "greater than 1%"
    title = 'Days with log errors greater than 1 percent'
    query3 = ("select errors.date, errors.num as total_errors, request.num as "
              "total_request, "
              "ROUND(errors.num * 100.0 / request.num) as percent from "
              "(select time::date as date, count(*) as num from log where "
              "status != '200 OK' "
              "group by date) as errors, "
              "(select time::date as date, count(*) as num from log "
              "group by date) as request "
              "where errors.date = request.date "
              "and errors.num * 100.0 / request.num > 1")
    run_query = news_query(query3)
    print("    " + title)
    for i in range(len(run_query)):
        print(' {}: date: {}, Percent of log errors: {}'
              .format(i+1, run_query[i][0], run_query[i][3]))


def run_querys():
    popular_articles()
    print('\n')
    popular_authors()
    print('\n')
    log_errors()


run_querys()
