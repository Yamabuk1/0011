# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 09:22:17 2022

@author: 山吹久远
"""

from tkinter import *

midvalue = 0

root=Tk()
root.geometry("800x600+200+200")

label1=Label(root,text="通用电流计",font=("微软雅黑","30"),fg="black",bg="white")
label1.pack()

label2=Label(root,text="请选择你的电路",font=("微软雅黑","15"),fg="black",bg="white")
label2.pack()

label1.place(relx=0.33,rely=0.0,relheight=0.12,relwidth=0.35)
label2.place(relx=0.38,rely=0.14,relheight=0.05,relwidth=0.25)

#主标题和副标题设置

def callback():
    print("0011")

def laststep():
    print(" ")
    
def Firststep():
    print(" ")

def choosebutton():
    global midvalue
    dic = {1:"1",2:"2"}
    s = dic.get(var.get())
    #print(s)
    midvalue = s
    #print(midvalue)
    

def cal():
    R1 = float(inpR1.get())
    R2 = float(inpR2.get())
    R3 = float(inpR3.get())
    R4 = float(inpR4.get())
    U = float(inpvoltage.get())
    #print("现在的midvalue是"+str(midvalue))
    if midvalue == "1":
        fvalue = U/R4+(R1+R3)*R4*U/(R1*R2+R1*R3+R2*R3)
        fvalue1 = round(fvalue,3)
        lb.config(text = fvalue1)
    else:
        fvalue = U/R3+(R4+R2)*R3*U/(R4*R1+R4*R2+R1*R2)
        fvalue2 = round(fvalue,3)
        lb.config(text = fvalue2)

def popupmenu(event):
    mainmenu.post(event.x_root,event.y_root)

#一堆函数

mainmenu = Menu(root) 
menubefore = Menu(mainmenu)
mainmenu.add_command(label = "上一步",command = laststep)

menuFirst = Menu(root)
mainmenu.add_command(label = "重来",command = Firststep)

#窗口上方选择目录

var = IntVar()
rd1 = Radiobutton(root,text="",variable=var,value=1,command=choosebutton)
rd1.pack()

rd2 = Radiobutton(root,text="",variable=var,value=2,command=choosebutton)
rd2.pack()

rd1.place(relx=0.05,rely=0.2,relheight=0.12,relwidth=0.1)
rd2.place(relx=0.45,rely=0.2,relheight=0.12,relwidth=0.1)


photo1 = PhotoImage(file="current1.gif")
imgLabel1 = Label(root,image=photo1)
imgLabel1.pack()

photo2 = PhotoImage(file="current2.gif")
imgLabel2 = Label(root,image=photo2)
imgLabel2.pack()

imgLabel1.place(relx=0.15,rely=0.2)
imgLabel2.place(relx=0.555,rely=0.2)

Label3 = Label(root,text="输入参数:",font=("微软雅黑","15"),fg="black",bg="white")
Label3.pack()
Label3.place(relx=0.07,rely=0.53,relheight=0.06,relwidth=0.15)

Labelvoltage = Label(root,text="电压/V",font=("微软雅黑","15"),fg="black",bg="white")
Labelvoltage.pack()
Labelvoltage.place(relx=0.27,rely=0.53,relheight=0.06,relwidth=0.10)

inpvoltage = Entry(root)
inpvoltage.place(relx=0.38,rely=0.54,relheight=0.05,relwidth=0.15)

LabelR1 = Label(root,text="R1/Ω",font=("微软雅黑","15"),fg="black",bg="white")
LabelR1.pack()
LabelR1.place(relx=0.15,rely=0.63,relheight=0.06,relwidth=0.10)

inpR1 = Entry(root)
inpR1.place(relx=0.25,rely=0.63,relheight=0.05,relwidth=0.15)

LabelR2 = Label(root,text="R2/Ω",font=("微软雅黑","15"),fg="black",bg="white")
LabelR2.pack()
LabelR2.place(relx=0.555,rely=0.63,relheight=0.06,relwidth=0.10)

inpR2 = Entry(root)
inpR2.place(relx=0.655,rely=0.63,relheight=0.05,relwidth=0.15)

LabelR3 = Label(root,text="R3/Ω",font=("微软雅黑","15"),fg="black",bg="white")
LabelR3.pack()
LabelR3.place(relx=0.15,rely=0.73,relheight=0.06,relwidth=0.10)

inpR3 = Entry(root)
inpR3.place(relx=0.25,rely=0.73,relheight=0.05,relwidth=0.15)

LabelR4 = Label(root,text="R4/Ω",font=("微软雅黑","15"),fg="black",bg="white")
LabelR4.pack()
LabelR4.place(relx=0.555,rely=0.73,relheight=0.06,relwidth=0.10)

inpR4 = Entry(root)
inpR4.place(relx=0.655,rely=0.73,relheight=0.05,relwidth=0.15)

btn = Button(root,text="运算",command=cal)
btn.place(relx=0.395,rely=0.79,relheight=0.06,relwidth=0.15)

Label4 = Label(root,text="电流为:",font=("微软雅黑","15"),fg="black",bg="white")
Label4.pack()
Label4.place(relx=0.255,rely=0.86,relheight=0.06,relwidth=0.15)

lb = Label(root,text='',font=("微软雅黑","15"),fg="blue",bg="white")
lb.pack()
lb.place(relx=0.405,rely=0.86,relheight=0.06,relwidth=0.15)

Label5 = Label(root,text="A",font=("微软雅黑","15"),fg="black",bg="white")
Label5.pack()
Label5.place(relx=0.555,rely=0.86,relheight=0.06,relwidth=0.15)

root.config(menu=mainmenu)
root.bind('Button-3',popupmenu)
root.mainloop()

#整一起