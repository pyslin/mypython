"""我们编写的Python代码会调用内置的Tkinter，Tkinter封装了访问Tk的接口；

Tk是一个图形库，支持多个操作系统，使用Tcl语言开发；

Tk会调用操作系统提供的本地GUI接口，完成最终的GUI。

所以，我们的代码只需要调用Tkinter提供的接口就可以了
"""
"""
from tkinter import *

#从Frame派生一个Application类，这是所有Widget的父容器
class Application(Frame):
    def __init__(self,master=None):
        #实现init，调用pack（）和createWidgets()
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self,text='Hello world!')
        self.helloLabel.pack()
        self.quitButton = Button(self,text='Quit',command=self.quit)
        self.quitButton.pack()


#在GUI中，每个Button、Label、输入框等，都是一个Widget。
# Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树

#实例化，并启动消息循环
app = Application()
# 设置窗口标题:
app.master.title('Hello world')
# 主消息循环:
app.mainloop()
"""

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()


    def createWidgets(self):
        #输入框
        self.nameInput = Entry(self)
        self.nameInput.pack()
        #按钮，command是点击后执行的东西
        self.alertButton = Button(self,text='Hello',command=self.hello)
        self.alertButton.pack()

    def hello(self):
        #取得输入框的内容
        name = self.nameInput.get() or 'world'
        #显示消息 ，消息标题和内容
        messagebox.showinfo('Message','Hello,%s'%name)

app = Application()


app.master.title('Hello world')
app.mainloop()

