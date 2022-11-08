def style(window,s,x,y):
    s.configure("title.TLabel",anchor="center",font=("Courier New",
                int(-y*0.085)))
    s.configure("time.TLabel",anchor="center",font=("Courier New",
                int(-y*0.145)))
    s.configure("highscore.TLabel",font=("Courier New",int(-y*0.044)))
    s.configure("dialog.TLabel",font=("Courier New",int(-y*0.045)),
                             justify="center",anchor="center")
    s.configure("options.TButton",font=("Courier New",int(-y*0.04)))
    s.configure("smallOptions.TButton",font=("Courier New",int(-y*0.033)))

def color(square,row,column,opened,flagged,mined,hovering,ended):
    if mined and ended and not opened:
        color = "gray25"
    elif hovering and not opened and not flagged:
        color = "gray95"
    elif (not hovering and not opened) or (hovering and flagged):
        color = "gray40" if (row+column)%2 else "gray45"
    else:
        color = "gray70" if (row+column)%2 else "gray80"
    square.config(bg=color)

def flag(square,thickness,nearStart,nearEnd,start,end,middle):
    square.create_line(nearStart,start,nearStart,end,width=thickness,
                       tags=("flag","f1"))
    square.create_polygon(nearStart,start,nearEnd,middle//2,
                          nearStart,middle,fill="black",tags=("flag","f2"))

def mine(square,thickness,nearStart,nearEnd,start,end,middle):
    square.create_oval(nearStart,nearStart,nearEnd,nearEnd,fill="black",
                       tags=("mine","m1"))
    square.create_line(middle,start,middle,end,width=thickness,
                       tags=("mine","m2"))
    square.create_line(start,middle,end,middle,width=thickness,
                       tags=("mine","m3"))
    square.create_line(nearStart,nearStart,nearEnd,nearEnd,width=thickness,
                       tags=("mine","m4"))
    square.create_line(nearStart,nearEnd,nearEnd,nearStart,width=thickness,
                       tags=("mine","m5"))

def x(square,thickness,nearStart,nearEnd):
    square.create_line(nearStart,nearStart,nearEnd,nearEnd,width=thickness*3,
                       fill="gray25",tags=("x","x1"))
    square.create_line(nearStart,nearEnd,nearEnd,nearStart,width=thickness*3,
                       fill="gray25",tags=("x","x2"))

def text(square,middle,fontSize,number):
    square.create_text((middle,middle),text=number,tags="number",
                        font=("Courier New",fontSize))

def redraw(square,thickness,nearStart,nearEnd,start,end,middle,fontSize):
    square.coords("number",middle,middle)
    square.itemconfigure("number",font=("Courier New",fontSize))

    square.coords("f1",nearStart,end,nearStart,start)
    square.coords("f2",nearStart,start,end,middle//2,nearStart,middle)
    square.itemconfigure("f1",width=thickness)

    square.itemconfigure("mine",width=thickness)
    square.coords("m1",nearStart,nearStart,nearEnd,nearEnd)
    square.coords("m2",middle,start,middle,end)
    square.coords("m3",start,middle,end,middle)
    square.coords("m4",nearStart,nearStart,nearEnd,nearEnd)
    square.coords("m5",nearStart,nearEnd,nearEnd,nearStart)

    square.itemconfigure("x",width=thickness*2)
    square.coords("x1",nearStart,nearStart,nearEnd,nearEnd)
    square.coords("x2",nearStart,nearEnd,nearEnd,nearStart)