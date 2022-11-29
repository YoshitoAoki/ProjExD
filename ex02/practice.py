import tkinter as tk

root = tk.Tk()
root.geometry("300x500")
w,h = 0,0
for b in range(9,-1,-1):
    button = tk.Button(root,text=b,font=("",30),width=4,height=2)
    button.grid(row=w,column=h )
    h+=1
    if h%3==0:
        w+=1
        h=0

root.mainloop()