from tkinter import *
from tkinter.messagebox import *
import sqlite3
from tkinter import ttk

dbstr = "/Users/mac/PycharmProjects/pythonProject1/sql3/mydb.db"

root = Tk()
root.geometry('700x1000')
root.title('学生画像系统')

Label(root, text="姓名：").place(relx=0, rely=0.05, relwidth=0.1)
Label(root, text="身高：").place(relx=0.5, rely=0.05, relwidth=0.1)
Label(root, text="体重：").place(relx=0, rely=0.1, relwidth=0.1)
Label(root, text="爱好：").place(relx=0.5, rely=0.1, relwidth=0.1)

name = StringVar()
weight = StringVar()
height = StringVar()
hobby = StringVar()
Entry(root, textvariable=name).place(relx=0.1, rely=0.05, relwidth=0.37, height=25)
Entry(root, textvariable=weight).place(relx=0.6, rely=0.05, relwidth=0.37, height=25)
Entry(root, textvariable=height).place(relx=0.1, rely=0.1, relwidth=0.37, height=25)
Entry(root, textvariable=hobby).place(relx=0.6, rely=0.1, relwidth=0.37, height=25)

Label(root, text='学生信息管理', bg='white', fg='red', font=('宋体', 15)).pack(side=TOP, fill='x')

def showAllInfo():
    x = dataTreeview.get_children()
    for item in x:
        dataTreeview.delete(item)

    try:
        con = sqlite3.connect(dbstr)
        cur = con.cursor()
        cur.execute("SELECT * FROM student")
        lst = cur.fetchall()
        for item in lst:
            dataTreeview.insert("", 1, text="line1", values=item)
    except Exception as e:
        print(e)
        con.rollback()
        print('查询数据库%s失败' % (dbstr))
    finally:
        cur.close()
        con.close()


def appendInfo():
    if name.get() == "":
        showerror(title='提示', message='输入不能为空')
    elif weight.get() == "":
        showerror(title='提示', message='输入不能为空')
    elif height.get() == "":
        showerror(title='提示', message='输入不能为空')
    elif hobby.get() == "":
        showerror(title='提示', message='输入不能为空')
    else:
        x = dataTreeview.get_children()
        for item in x:
            dataTreeview.delete(item)
        list1 = []
        list1.append(name.get())
        list1.append(weight.get())
        list1.append(height.get())
        list1.append(hobby.get())
        con = sqlite3.connect(dbstr)
        cur = con.cursor()
        cur.execute("insert into student values" + str(tuple(list1)))
        con.commit()
        cur.execute("select * from student")
        lst = cur.fetchall()
        for item in lst:
            dataTreeview.insert("", 1, text="line1", values=item)
        cur.close()
        con.close()


def deleteInfo():
    con = sqlite3.connect(dbstr)
    cur = con.cursor()
    cur.execute("select * from student")
    studentList = cur.fetchall()
    cur.close()
    con.close()
    print(studentList)
    try:
        nam = str(name.get())
        con = sqlite3.connect(dbstr)
        cur = con.cursor()
        cur.execute("delete from student where name = '%s'"%(nam))
        con.commit()
        showinfo(title='提示', message='删除成功！')
    except Exception as e:
        print(e)
        showerror(title='提示', message='删除失败')
    finally:
        cur.close()
        con.close()
    x = dataTreeview.get_children()
    for item in x:
        dataTreeview.delete(item)
    con = sqlite3.connect(dbstr)
    cur = con.cursor()
    cur.execute("select * from student")
    lst = cur.fetchall()
    for item in lst:
        dataTreeview.insert("", 1, text="line1", values=item)
    cur.close()
    con.close()


Button(root, text="显示所有信息", command=showAllInfo).place(relx=0.2, rely=0.2, width=100)
Button(root, text="追加信息", command=appendInfo).place(relx=0.4, rely=0.2, width=100)
Button(root, text="删除信息", command=deleteInfo).place(relx=0.6, rely=0.2, width=100)

dataTreeview = ttk.Treeview(root, show='headings', column=('name', 'weight', 'height', 'hobby'))
dataTreeview.column('name', width=150, anchor="center")
dataTreeview.column('weight', width=150, anchor="center")
dataTreeview.column('height', width=150, anchor="center")
dataTreeview.column('hobby', width=150, anchor="center")

dataTreeview.heading('name', text='姓名')
dataTreeview.heading('weight', text='身高')
dataTreeview.heading('height', text='体重')
dataTreeview.heading('hobby', text='爱好')

dataTreeview.place(rely=0.3, relwidth=0.97)
root.mainloop()  # 界面运行