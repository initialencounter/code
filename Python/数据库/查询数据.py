import sqlite3
con = sqlite3.connect('./demo1.db')
cur = con.cursor()
sql = 'select * from t_person'
try:
    cur.execute(sql)
    re = cur.fetchall()
    for i in re:
        print(i)
except Exception as e:
    print(e)
    con.rollback()
    print(0)
finally:
    cur.close()
    con.close()