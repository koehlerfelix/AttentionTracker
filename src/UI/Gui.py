from tkinter import *
import threading
import src.eyetracker.connection as c

window = Tk()

windowX = 1500
windowY = 750

window.title("Attention Assistnace")
window.geometry("%dx%d+0+0" % (windowX, windowY))

def openNewWindow():
    lbl.configure(text = "Warum klickst du auf Fertig?? Du bist doch noch nicht fertig!!! :(")

def start_Collecting():
    thread.start()

def finish_Collecting():
    thread.join(1)
    c.stop_collecting()
    print("Alles fertig!")

def thread_work():
    while(1):
        c.start_collecting()


thread = threading.Thread(target=thread_work)

lbl = Label(window, text="Text", font=("Arial Bold", 10))
lbl.pack(side=TOP)

btnFin = Button(window, text="Fertig", command=finish_Collecting)

btnFin.place(x=windowX - 50, y=windowY - 30)

btnStart = Button(window, text="Start", command=start_Collecting)

btnStart.place(x=10, y=windowY - 30)



window.mainloop()