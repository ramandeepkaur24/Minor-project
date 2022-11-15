
#emergency content

from tkinter import *
window = Tk()
window.configure(bg='white')
window.geometry('400x480')

canvas = Canvas(window,height=500,width=400)
canvas.configure(bg='white')


srno_lb = Label(window, text="SR_NO", width=7, height=2, borderwidth=3, relief="ridge", font="20", bg="white")
srno_lb.place(x=2, y=10)

name_lb = Label(window, text="NAME", width=20, height=2, borderwidth=3, relief="ridge", bg="white", font="20")
name_lb.place(x=95, y=10)

connum_lb = Label(window, text="CONTECT", width=10, height=2, borderwidth=3, relief="ridge", bg="white",
                  font="20")
connum_lb.place(x=300, y=10)

class one():
    lb1 = Label(window, text="1.", font="15", bg="white")
    lb1.place(x=35, y=64)

    lb1 = Label(window, text="POLICE", font="15", bg="white")
    lb1.place(x=98, y=64)

    one = Button(window, text="call", borderwidth=2)
    one.place(x=340, y=63)

class two():
    lb2 = Label(window, text="2.", font="15", bg="white")
    lb2.place(x=35, y=104)

    lb2 = Label(window, text="AMBULANCE", font="15", bg="white")
    lb2.place(x=98, y=104)

    two = Button(window, text="call", borderwidth=2)
    two.place(x=340, y=103)

class three():
    lb2 = Label(window, text="3.", font="15", bg="white")
    lb2.place(x=35, y=144)

    lb2 = Label(window, text="WOMEN HELPLINE", font="15", bg="white")
    lb2.place(x=98, y=144)

    two = Button(window, text="call", borderwidth=2)
    two.place(x=340, y=141)


class four():
    lb2 = Label(window, text="4.", font="15", bg="white")
    lb2.place(x=35, y=184)

    lb2 = Label(window, text="TRAFFIC HELPLINE", font="15", bg="white")
    lb2.place(x=98, y=184)

    two = Button(window, text="call", borderwidth=2)
    two.place(x=340, y=181)

class five():
    lb2 = Label(window, text="5.", font="15", bg="white")
    lb2.place(x=35, y=224)

    lb2 = Label(window, text="FIRE DEPARTMENT", font="15", bg="white")
    lb2.place(x=98, y=224)

    two = Button(window, text="call", borderwidth=2)
    two.place(x=340, y=221)

class six():
    lb2 = Label(window, text="6.", font="15", bg="white")
    lb2.place(x=35, y=264)

    lb2 = Label(window, text="RAILWAY", font="15", bg="white")
    lb2.place(x=98, y=264)

    two = Button(window, text="call", borderwidth=2)
    two.place(x=340, y=261)

class seven():
    lb2 = Label(window, text="7.", font="15", bg="white")
    lb2.place(x=35, y=304)

    lb2 = Label(window, text="CYBER CRIME HELPLINE", font="15", bg="white")
    lb2.place(x=98, y=304)

    two = Button(window, text="call", borderwidth=2)
    two.place(x=340, y=301)

class eight():
    lb2 = Label(window, text="8.", font="15", bg="white")
    lb2.place(x=35, y=344)

    lb2 = Label(window, text="CENTRALISED HELPLINE", font="15", bg="white")
    lb2.place(x=98, y=344)

    two = Button(window, text="call", borderwidth=2)
    two.place(x=340, y=341)

class nine():
    lb2 = Label(window, text="9.", font="15", bg="white")
    lb2.place(x=35, y=384)

    lb2 = Label(window, text="CHILD HELPLINE", font="15", bg="white")
    lb2.place(x=98, y=384)

    two = Button(window, text="call", borderwidth=2)
    two.place(x=340, y=381)

class ten():
    lb2 = Label(window, text="10.", font="15", bg="white")
    lb2.place(x=35, y=424)

    lb2 = Label(window, text="ANTI CORRPUTION\n HELPLINE", font="15", bg="white")
    lb2.place(x=98, y=424)

    two = Button(window, text="call", borderwidth=2)
    two.place(x=340, y=428)


canvas.create_line(80,0,80,500,fill="black") #horizontal line 1
canvas.create_line(296,0,296,500,fill="black") #horizontal line 2
canvas.create_line(0,57,400,57,fill="black") #vertical line 1
canvas.create_line(0,95,400,95,fill="black") #vertical line 2
canvas.create_line(0,135,400,135,fill="black") #vertical line 3
canvas.create_line(0,175,400,175,fill="black") #vertical line 4
canvas.create_line(0,215,400,215,fill="black") #vertical line 5
canvas.create_line(0,255,400,255,fill="black") #vertical line 6
canvas.create_line(0,295,400,295,fill="black") #vertical line 7
canvas.create_line(0,335,400,335,fill="black") #vertical line 8
canvas.create_line(0,375,400,375,fill="black") #vertical line 9
canvas.create_line(0,415,400,415,fill="black") #vertical line 10
canvas.create_line(0,470,400,470,fill="black") #vertical line 11







canvas.pack()



window.mainloop()