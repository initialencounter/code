import sqlite3
def new_table1(DB_Name = './mydb.db',Table_Name = 'student'):
    conn = sqlite3.connect(DB_Name)

    try:
        cursor = conn.cursor()
        SQL = 'CREATE TABLE %s(name,weight,height,hobby,PRIMARY KEY(name))'%(Table_Name)
        cursor.execute(SQL)
        conn.commit()
        print('创建数据库表%s成功'%(Table_Name))
    except Exception as e:
        print(e)
        conn.rollback()
        print('创建数据库%s失败'%(Table_Name))
    finally:
        conn.close()

def db_insert(DB_Name = './mydb.db',Table_Name = 'student'):
    conn = sqlite3.connect(DB_Name)
    name1 = 'wc'
    number1 = '1331'
    name2 = 'prince'
    number2 = '1231'
    try:
        cursor = conn.cursor()
        list = ['12' ,14,1,123]
        print("insert into student values" + str(tuple(list)))
        # SQL = "insert into %s values('%s','%s'),('%s','%s')" %(Table_Name,name1,number1,name2,number2)
        SQL = "insert into student values" + str(tuple(list))
        cursor.execute(SQL)
        conn.commit()
        print('插入到数据库表%s成功' % (Table_Name))
    except Exception as e:
        print(e)
        conn.rollback()
        print('插入到数据库%s失败' % (Table_Name))
    finally:
        conn.close()



def db_index(DB_Name = './mydb.db',Table_Name = 'student'):
    conn = sqlite3.connect(DB_Name)
    SQL_table = Table_Name
    try:
        cursor = conn.cursor()
        SQL = "SELECT * FROM %s"%(SQL_table)
        cursor.execute(SQL)
        #获取一条数据
        # one = cursor.fetchone()
        # print(one)
        #获取所有数据
        for row in cursor.fetchall():
            print(row)

    except Exception as e:
        print(e)
        conn.rollback()
        print('查询数据库%s失败' % (Table_Name))
    finally:
        conn.close()


def db_update(DB_Name = './mydb.db',Table_Name = 'student'):
    conn = sqlite3.connect(DB_Name)
    SQL_table = Table_Name.upper()
    try:
        cursor = conn.cursor()
        SELECT_SQL = "SELECT * FROM %s" % (SQL_table)
        UPDATE_SQL = "UPDATE %s SET SNAME ='%s' WHERE SNO = '%s'"%(SQL_table,'小王','wc')

        print('修改前')
        cursor.execute(SELECT_SQL)
        for row in cursor.fetchall():
            print(row)

        print('修改后')
        cursor.execute(UPDATE_SQL)
        conn.commit()
        cursor.execute(SELECT_SQL)
        for row in cursor.fetchall():
            print(row)

    except Exception as e:
        print(e)
        conn.rollback()
        print('插入到数据库%s失败' % (Table_Name))
    finally:
        conn.close()


def db_delete(DB_Name = './mydb.db',Table_Name = 'student'):
    conn = sqlite3.connect(DB_Name)
    SQL_table = Table_Name.upper()
    try:
        cursor = conn.cursor()
        nam = str(12)
        SELECT_SQL = "select * from %s" % (SQL_table)
        UPDATE_SQL = "delete from '%s' where name = '%s'"%(SQL_table,nam)
        print("delete from '%s' where name = '%s'"%(SQL_table,'12'))

        print('删除前')
        cursor.execute(SELECT_SQL)
        for row in cursor.fetchall():
            print(row)

        print('删除后')
        cursor.execute(UPDATE_SQL)
        conn.commit()
        cursor.execute(SELECT_SQL)
        for row in cursor.fetchall():
            print(row)

    except Exception as e:
        print(e)
        conn.rollback()
        print('插入到数据库%s失败' % (Table_Name))
    finally:
        conn.close()

def new_table(DB_Name = './mydb.db',Table_Name = 'student'):
    conn = sqlite3.connect(DB_Name)

    try:
        cursor = conn.cursor()
        num = 12
        cursor.execute("delete from student where name = "+num)
        conn.commit()
        print('创建数据库表%s成功'%(Table_Name))
    except Exception as e:
        print(e)
        conn.rollback()
        print('创建数据库%s失败'%(Table_Name))
    finally:
        conn.close()


# new_table()
# db_insert()
# db_index(DB_Name = './mydb.db',Table_Name = 'student')
# db_update(DB_Name = './mydb.db',Table_Name = 'student')
# db_delete(DB_Name = './mydb.db',Table_Name = 'student')
def col():
    for i in range(3):
        print('i='+str(i))
        for j in range(2):
            print(j)
    print('d')
# col()

for i in range(2):
    print('i = '+str(i))
    for j in range(3):
        print(' j = '+str(j))
print('done!')


