# Log Analysis
The Log Analysis is an internal reporting tool. The reporting tool uses
information from a database with news articles to determine which articles
the site's readers like

## Questions given to the reporting tool
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

# Getting Started

## PreRequisites
1. Virtual Machine: Vagrant
2. Python3

## Running the Log Analysis reporting tool
# In the terminal:
  * first confirm the reporting tool is in the vagrant folder
  * cd to log_analysis folder
  * afterwards us $ vagrant up
  * followed by $ vagrant ssh
  * run the tool $ python3 newsdata.py
  * The queries will now be displayed in the terminal


# File descriptions
* newsdata.sql: Holds the news database. The news database has the following three
  tables: Authors, Articles, Log.
* newsdata.py: Here is the python code needed to access the news database to answer
  the three questions.
* results.txt: Has a copy of the text printed in the terminal after running
  newsdata.py
