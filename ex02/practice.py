import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    num = btn["text"]
    # tkm.showinfo("",f"{num}ボタンがクリックされました")
    entry.insert(tk.END,num)

root = tk.Tk()
root.geometry("300x500")

entry = tk.Entry(root,justify="right",width=10,font=("",40))
entry.grid(row=0,column=0,columnspan=3)

w,h = 1,0
for b in range(9,-1,-1):
    button = tk.Button(root,text=b,font=("",30),width=4,height=2)
    button.grid(row=w,column=h )
    button.bind("<1>",button_click)
    h+=1
    if h%3==0:
        w+=1
        h=0

operators = ["+","="]
for op in operators:
    button = tk.Button(root,text=f"{op}",width=4,height=2,font=("",30))
    button.grid(row=w,column=h)
    h+=1
    if h%3==0:
        w+=1
        h=0

root.mainloop()