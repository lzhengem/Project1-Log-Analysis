#!/usr/bin/python3

import datetime
import psycopg2

DBNAME = "news"

conn = psycopg2.connect(database=DBNAME)
cursor = conn.cursor()
cursor.execute('''select title,count(title)
    from authors_articles_log
    group by title
    order by count(title) desc''')
most_popular_title = cursor.fetchall()


cursor.execute('''select author_name , count(author_name)
    from authors_articles_log
    group by author_name
    order by count(author_name) desc''')
most_popular_author = cursor.fetchall()

cursor.execute('''select total_rec.date, ((errors/total) * 100)
    from (select time::date date, count(*)::decimal total
        from log
        group by date) total_rec
    join (select time::date date, count(*)::decimal errors
        from log
        where status not like ('200%')
    group by date) bad_rec on bad_rec.date = total_rec.date
    where ((errors/total) * 100) > 1''')
over_1_perc_error = cursor.fetchall()

conn.close()

for title, count in most_popular_title:
    print("{} - {} views".format(title, count))
print()

for title, count in most_popular_author:
    print("{} - {} views".format(title, count))
print()
for day, perc_errors in over_1_perc_error:
    print("{} - {:.1f}% errors".format(day, perc_errors))
