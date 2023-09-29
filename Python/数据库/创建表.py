import sqlite3
con = sqlite3.connect('./demo1.db')#创建连接
# print(con)
cur = con.cursor()#创建游标
sql = '''create table t_person(
            pno INTEGER primary key autoincrement,
            pname VERCHAR not null,
            age INTEGER
        )'''
try:
    cur.execute(sql)#执行
    print(1)
except Exception as e:
    print(e)
    print(0)
finally:
    cur.close()
    con.close()