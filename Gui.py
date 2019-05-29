from tkinter import *

window = Tk()

windowX = 1500
windowY = 750

window.title("Attention Assistnace")
window.geometry("%dx%d+0+0" % (windowX, windowY))

def openNewWindow():
    lbl.configure(text = "Warum klickst du auf Fertig?? Du bist doch noch nicht fertig!!! :(")


lbl = Label(window, text="Text", font=("Arial Bold", 10))
lbl.pack(side=TOP)

btnFin = Button(window, text="Fertig", command=openNewWindow)

btnFin.place(x=windowX - 50, y=windowY - 30)

btnStart = Button(window, text="Start")

btnStart.place(x=10, y=windowY - 30)



window.mainloop()