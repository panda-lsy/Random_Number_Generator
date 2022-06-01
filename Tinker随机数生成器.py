import tkinter as tk
import random as r

randoms=[]

window = tk.Tk()
window.title("随机数生成器:请输入随机数")       #窗口名称
window.geometry('350x175')                    #窗口大小
tk.Label(window,text="最小值",width=6).place(x=10,y=1)
input1=tk.Entry(window,show=None)                  #输入框
input1.pack()
tk.Label(window,text="最大值",width=6).place(x=10,y=20)
input2=tk.Entry(window,show=None)
input2.pack()
tk.Label(window,text="输出数量",width=6).place(x=10,y=40)
input3=tk.Entry(window,show=None)
input3.pack()
text=tk.Text(window,height=2).place(x=10,y=85)      #输出框
tk.Label(window,text="输出随机数",width=10).place(x=0,y=60)
def calculate(min,max,frequency):
    for i in range(0,frequency+1):
        randoms.append(r.randint(min,max))

def confirm():
    min=int(input1.get())
    max=int(input2.get())
    frequency=int(input3.get())
    calculate(min,max,frequency)
    for i in range(0,len(randoms)+1):
        numout=randoms[i]
        text.insert("end",numout)
    
#按钮
confirm = tk.Button(window,text="确定",width=15,height=2,command=confirm).place(x=100,y=120)




window.mainloop()
    
