from tkinter import *

import threading
import tobii_research as tr
import src.eyetracker.eyetracker as et

class GUI:
    global connected
    connected = False
    global eyetracker
    eyetracker = 0

    def run(self):

        window = Tk()

        windowX = 1500
        windowY = 750

        window.title("Attention Assistnace")
        window.state('zoomed')
        window.geometry("%dx%d+0+0" % (windowX, windowY))

        thread = threading.Thread(target=self.thread_work)

        lbl = Label(window, text="Text", font=("Arial Bold", 10))

        lbl.pack(side=TOP)

        btnFin = Button(window, text="Fertig", command=self.finish_Collecting(thread))

        btnFin.place(x=windowX - 50, y=windowY - 30)

        btnStart = Button(window, text="Start", command=self.start_Collecting(thread))

        btnStart.place(x=10, y=windowY - 30)

        btnConnect = Button(window, text="Connect", command=self.connect)

        btnConnect.place(x=windowX / 2, y=windowY - 30)

        window.mainloop()


    def openNewWindow(self, lbl):
        lbl.configure(text="Warum klickst du auf Fertig?? Du bist doch noch nicht fertig!!! :(")


    def start_Collecting(self, thread):
        if connected:
            thread.start()


    def finish_Collecting(self, thread):
        if connected:
            thread.join(1)
            global eyetracker
            eyetracker.stop_collecting()
            print("Alles fertig!")


    def thread_work(self):
        if connected:
            while (1):
                global eyetracker
                eyetracker.start_collecting()


    def connect(self):
        found_eyetrackers = tr.find_all_eyetrackers()

        if len(found_eyetrackers) == 0:
            print("No eyetrackers connected")
            # exit()
        else:
            my_eyetracker = found_eyetrackers[0]
            print("Address: " + my_eyetracker.address)
            print("Model: " + my_eyetracker.model)
            print("Name (It's OK if this is empty): " + my_eyetracker.device_name)
            print("Serial number: " + my_eyetracker.serial_number)
            global eyetracker
            eyetracker = et.Eyetracker(my_eyetracker)
            global connected
            connected = True



