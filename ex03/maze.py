import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root,width=1500,height=900,bg="black")

    koukaton = tk.PhotoImage(file="fig/8.png")
    cx,cy = 300,400
    canvas.create_image(cx,cy,image=koukaton,tag="こうかとん")

    canvas.pack()
    root.mainloop()