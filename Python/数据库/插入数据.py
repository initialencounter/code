import sqlite3

con = sqlite3.connect('./demo1.db')

cur = con.cursor()

sql = 'insert into t_person(pname,age) values(?,?)'


try:
    # cur.execute(sql,('张三',23))
    cur.executemany(sql,[('王武',23),('李四',11)])
    con.commit()
    print(1)
except Exception as e:
    print(e)
    con.rollback()
    print(0)
finally:
    cur.close()
    con.close()