from tkinter import *
from tkinter import messagebox
class Application(Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.creatwidget()

    def creatwidget(self):
        v1 = StringVar()
        self.entry1 = Entry(self,textvariable=v1).grid(row=0,column=0,columnspan=90)
        v1.set('12312312328364826498726948169846182649812694619286481236482368238')
        btntext = [['`',1,2,3,4,5,6,7,8,9,0,'-','=','back'],
                   ['tab','q','w','e','r','t','y','u','i','o','p','[',']','\\'],
                   ['中/音','a','s','d','f','g','h','j','k','l',';','"','enter'],
                   ['shift','z','x','c','v','b','n','m',',','.','/','shift'],
                   ['fn','cntrol','opt','cmd','space']]
        for rindex,r in enumerate(btntext):
            for cindex,c in enumerate(r):
                if c=='tab':
                    Button(self,text=c).grid(row=(rindex+1)*2,column=cindex*2,rowspan=2,columnspan=3,sticky=NSEW)
                elif c=='中/音':
                    Button(self, text=c).grid(row=(rindex+1)*2, column=cindex*2, rowspan=2, columnspan=3, sticky=NSEW)
                elif c=='bsck':
                    Button(self, text=c).grid(row=(rindex+1)*2, column=cindex*2, rowspan=2, columnspan=3, sticky=NSEW)
                elif c=='enter':
                    Button(self, text=c).grid(row=(rindex+1)*2, column=cindex*2, rowspan=2, columnspan=3, sticky=NSEW)
                elif c=='shift':
                    Button(self, text=c).grid(row=(rindex+1)*2, column=cindex*2, rowspan=2, columnspan=4, sticky=NSEW)
                elif c=='cmd':
                    Button(self, text=c).grid(row=(rindex+1)*2, column=cindex*2, rowspan=2, columnspan=1, sticky=NSEW)
                elif c=='space':
                    Button(self,text=c).grid(row=(rindex+1)*2,column=cindex*2,rowspan=2,columnspan=8,sticky=NSEW)
                else:
                    Button(self,text=c).grid(row=(rindex+1)*2,column=cindex*2,rowspan=2,columnspan=2,sticky=NSEW)

    def songhua(self):
        messagebox.showinfo('Message', '送你一朵小花花')

if __name__ == '__main__':

    root = Tk()
    root.title = '我的第一个GUI'
    root.geometry('2000x2000+50+50')
    app = Application(root)


    root.mainloop()