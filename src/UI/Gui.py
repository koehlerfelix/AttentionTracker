from tkinter import *

import threading
import tobii_research as tr
import src.eyetracker.eyetracker as et


class GUI:

    def __init__(self):
        trackers = tr.find_all_eyetrackers()
        if len(trackers) > 0:
            self.__eye_tracker = et.EyeTracker(trackers[0])
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

        frame = Frame(window, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)

        lbl = Label(frame, text="Text", font=("Arial Bold", 20), bg='black', fg='white', width=80, height=20)
        lbl.pack(expand='True', padx=5, pady=5)

        btn_stop = Button(text="Stop", command=self.stop_collecting).pack(side="right", padx=10, pady=5)
        btn_start = Button(text="Start", command=self.start_collecting).pack(side="left", padx=10, pady=5)
        btn_connect = Button(text="Connect", command=self.connect).pack(side="bottom", padx=10, pady=5)

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
            self.__eye_tracker = et.EyeTracker(my_eye_tracker)
            self.__connected = True

    def is_connected(self):
        return self.__connected


