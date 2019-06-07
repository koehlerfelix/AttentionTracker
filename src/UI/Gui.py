from tkinter import *

import threading
import tobii_research as tr
import src.eyetracker.eyetracker as et


class GUI:

    def __init__(self):
        trackers = tr.find_all_eyetrackers()
        if len(trackers) > 0:
            self.__eye_tracker = et.Eyetracker(trackers[0])
            self.__connected = True
        else:
            self.__connected = False
        self.__thread = threading.Thread(target=self.thread_work)

    def run(self):

        window = Tk()

        window_x = 1500
        window_y = 750

        window.title("Attention Assistance")
        window.state('zoomed')
        window.geometry("%dx%d+0+0" % (window_x, window_y))

        lbl = Label(window, text="Text", font=("Arial Bold", 10))

        lbl.pack(side=TOP)

        btn_stop = Button(window, text="Stop", command=self.stop_collecting)

        btn_stop.place(x=window_x - 50, y=window_y - 30)

        btn_start = Button(window, text="Start", command=self.start_collecting)

        btn_start.place(x=10, y=window_y - 30)

        btn_connect = Button(window, text="Connect", command=self.connect)

        btn_connect.place(x=window_x / 2, y=window_y - 30)

        window.mainloop()

    def start_collecting(self):
        if self.__connected:
            self.__thread.start()

    def stop_collecting(self):
        if self.__connected:
            self.__thread.join(1)
            self.__eye_tracker.stop_collecting()

    def thread_work(self):
        if self.__connected:
            self.__eye_tracker.start_collecting()

    def connect(self):
        if self.is_connected():
            return

        found_eye_trackers = tr.find_all_eyetrackers()

        if len(found_eye_trackers) == 0:
            print("No eye trackers connected")
            # exit()
        else:
            my_eye_tracker = found_eye_trackers[0]
            print("Address: " + my_eye_tracker.address)
            print("Model: " + my_eye_tracker.model)
            print("Name (It's OK if this is empty): " + my_eye_tracker.device_name)
            print("Serial number: " + my_eye_tracker.serial_number)
            print("Connection successful")
            self.__eye_tracker = et.Eyetracker(my_eye_tracker)
            self.__connected = True

    def is_connected(self):
        return self.__connected


