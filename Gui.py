from tkinter import *

window = Tk()

windowX = 1200
windowY = 700

window.title("Attention Assistnace")
window.geometry("%dx%d" % (windowX, windowY))

lbl = Label(window, text="Text", font=("Arial Bold", 10))
lbl.pack(side=TOP)

btnFin = Button(window, text="Fertig", command=window.quit)

btnFin.place(x=windowX - 50,y=windowY - 30)

btnStart = Button(window, text="Start")

btnStart.place(x=10,y=windowY - 30)


window.mainloop()