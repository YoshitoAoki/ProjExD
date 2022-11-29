import tkinter as tk
import tkinter.messagebox as tkm

g = ""

def button_click(event):
    btn = event.widget
    num = btn["text"]
    # tkm.showinfo("",f"{num}ボタンがクリックされました")
    if num == "=":
        s = entry.get()
        ans = eval(s)
        entry.delete(0,tk.END)
        entry.insert(tk.END,ans)
        pass
    else:
        entry.insert(tk.END,num)

def Enter_col(event):
    event.widget["bg"] = "#e6e6fa"
    event.widget["fg"] = "white"

def Def_col(event):
    event.widget["bg"] = "white"
    event.widget["fg"] = "black"

def Memory(event):
    ev = event.widget
    val = ev["text"]
    global g
    if val == "M+":
        g = entry.get()
        g = g.replace("+","")
    
    if val == "MR":
        print("MRが押されました")
        print(g)
        entry.insert(tk.END,g)

def Clear(event):
    entry.delete(0,tk.END)


root = tk.Tk()
root.geometry("400x500")

entry = tk.Entry(root,justify="right",width=14,font=("",40))#入力欄生成
entry.grid(row=0,column=0,columnspan=20)

w,h = 1,0
for b in range(9,-1,-1):#数字ボタン生成
    button = tk.Button(root,text=b,font=("",30),width=4,height=2)
    button.grid(row=w,column=h )
    button.bind("<1>",button_click)
    h+=1
    if h%3==0:
        w+=1
        h=0

operators = ["+","="]
for op in operators:#＋＝ボタン生成
    button = tk.Button(root,text=f"{op}",width=4,height=2,font=("",30))
    button.grid(row=w,column=h)
    button.bind("<1>",button_click)
    button.bind("<Enter>",Enter_col)
    button.bind("<Leave>",Def_col)
    h+=1
    if h%3==0:
        w+=1
        h=0

memory = ["M+","MR"]
r=1
for m in memory:#M+、MRボタン生成
    button = tk.Button(root,text=f"{m}",width=4,height=2,font=("",30))
    button.grid(row=r,column=4)
    button.bind("<1>",Memory)
    r += 1


clear = tk.Button(root,text="C",width=4,height=2,font=("",30),bg="red",fg="white")
clear.grid(row=3,column=4)
clear.bind("<1>",Clear)

root.mainloop()