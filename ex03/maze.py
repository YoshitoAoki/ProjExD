import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym
    if key == "s" and flag == 0:
        start()


def key_up(event):
    global key
    key = ""


def main_proc():
    global cx, cy,mx,my
    if key == "Up": my -= 1
    if key == "Down": my += 1
    if key == "Left": mx -= 1
    if key == "Right": mx += 1
    if maze_lst[mx][my] == 1:
        if key == "Up": my += 1
        if key == "Down": my -= 1
        if key == "Left": mx += 1
        if key == "Right": mx -= 1
    cx,cy = mx*100+50, my*100+50
    canvas.coords("kokaton", cx, cy)
    root.after(200, main_proc)

def timer():
    global tmr
    label["text"] = f"Time:{tmr}秒"
    tmr += 1
    jid = root.after(1000,timer)

def start():
    global flag
    flag = 1
    if key == "s":
        timer()
        main_proc()




# def goal():
#     pass
        


if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    flag = 0
    tmr = 0
    label = tk.Label(root,font=("",45),fg="black",bg="white")
    label.place(x=1150,y=20)

    maze_lst = mm.make_maze(15,9)
    mm.show_maze(canvas,maze_lst)
    # print(maze_list)

    mx,my = 1,1
    cx,cy = mx*100+50, my*100+50
    tori = tk.PhotoImage(file="fig/8.png")
    canvas.create_image(cx, cy, image=tori, tag="kokaton")
    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    
    
    root.mainloop()