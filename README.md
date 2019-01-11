# Introduction
project1_logs_analysis.py answers 3 questions from the news database provided by Udacity:
* What are the most popular three articles of all time?
    - (sorted list with most popular on top)
* Who are the most popular article authors of all time?
   - (sorted list with most popular on top)
* On which days did more than 1% of requests lead to errors? 

## Installation
* This program uses python3
* This program uses psql, so needs dependency psycopg2
    ```pip3 install psycopg2```
* The data is from Udacity's [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) file
* A view is used in this program:

```
CREATE VIEW authors_articles_log as
    select name author_name, title
    from authors
    left join articles on articles.author = authors.id
    left join (select * from log where path like '/article/%') log 
                on substr(path,10) = articles.slug
    order by authors.name;
```

## Description
* The view authors_articles_log has the articles, its author, and their path. It is used to calculate the most popular author and articles based on sucessfull path visits.
* To find days where more than 1% lead to errors, we count the error statuses for each day and divide it by the total count of requests.
* The results from these answers are printed onto the terminal

## Usage
`python3 project1_logs_analysis.py`

Example output:
```
    Candidate is jerk, alleges rival - 338647 views
    Bears love berries, alleges bear - 253801 views
    Bad things gone, say good people - 170098 views
    ...
```