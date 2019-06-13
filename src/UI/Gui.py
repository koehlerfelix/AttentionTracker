from tkinter import *

import threading
import tobii_research as tr
import src.eyetracker.eyetracker as eyetracker


class GUI:


    def __init__(self):
        trackers = tr.find_all_eyetrackers()
        if len(trackers) > 0:
            self.__eye_tracker = eyetracker.EyeTracker(trackers[0])
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

        # taking image from the directory and storing the source in a variable
        page1 = PhotoImage(file="images/Beispiel.png")
        page1 = page1.subsample(2,2)

        page2 = PhotoImage(file="images/Beispiel2.png")
        page2 = page2.subsample(2, 2)

        # displaying the picture using a 'Label' by passing the 'picture' variriable to 'image' parameter
        label = Label(frame, image=page1, width=1300, height=750)

        #lbl = Label(frame, text="Text", font=("Arial Bold", 20), bg='black', fg='white', width=80, height=20)
        #lbl.plack(expand='True', padx=5, pady=5)

        btn_stop = Button(text="Stop", command=self.stop_collecting).pack(side="left", padx=10, pady=5)
        btn_start = Button(text="Start", command=self.start_collecting).pack(side="left", padx=10, pady=5)
        btn_connect = Button(text="Connect", command=self.connect).pack(side="left", padx=10, pady=5)

        btn_next = Button(text="next Page", command=lambda: self.next_page(label, page2)).pack(side="left")
        btn_previous = Button(text="previous Page", command=lambda: self.next_page(label, page1)).pack(side="left")

        label.pack(expand='True')

        window.mainloop()

    def next_page(self, label, page):
        label.config(image=page)

    def start_collecting(self):
        if self.__connected:
            self.__thread.start()

    def stop_collecting(self):
        if self.__connected:
            self.__thread.join(1)
            self.__eye_tracker.stop_collecting()
            print(eyetracker.get_gaze_data())

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
            self.__eye_tracker = eyetracker.EyeTracker(my_eye_tracker)
            self.__connected = True

    def is_connected(self):
        return self.__connected


