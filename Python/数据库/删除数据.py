import sqlite3
con = sqlite3.connect('./demo1.db')
cur = con.cursor()
sql = 'delete from t_person where pno=(?)'

try:
    cur.execute(sql,(3,))
    con.commit()
    print(1)
except Exception as e:
    print(e)
    con.rollback()
    print(0)
finally:
    cur.close()
    con.close()