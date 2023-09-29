import sqlite3
con = sqlite3.connect('./demo1.db')
cur = con.cursor()
sql = 'update t_person set pname=(?) where pno=(?)'

try:
    cur.execute(sql,('小米',1))
    con.commit()
    print(1)
except Exception as e:
    print(e)
    con.rollback()
    print(0)
finally:
    cur.close()
    con.close()