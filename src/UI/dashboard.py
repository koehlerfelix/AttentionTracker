import tkinter as tk
from tkinter import *


class Dashboard(tk.Toplevel):

    # gaze data list hat 2 listen: [0] hat keine "NaN" werte [1] hat welche

    def __init__(self, gaze_data_list, avg_pupil_size, pupil_data_list):
        self.__gaze_data_list = gaze_data_list
        self.__pupil_data_list = pupil_data_list
        self.__avg_pupil_size = avg_pupil_size

        tk.Toplevel.__init__(self)

        window_x = self.winfo_screenwidth()
        window_y = self.winfo_screenheight()

        self.title('Attention Assistance Results')
        self.state('zoomed')
        self.geometry("%dx%d+0+0" % (window_x - 100, window_y - 100))

        self.configure(background='#111111')

        # create frame
        frame = Frame(self, borderwidth=1, background='#1E1E1E')
        frame.pack(fill=BOTH, expand=True)

        # making canvas
        self.__canvas = Canvas(frame, width=window_x - 130, height=window_y - 230, background='white')
        self.__canvas.pack(expand='True')

        # loding image into canvas !!!!not working!!!! and i have no clue why
        img = PhotoImage(file="images/Beispiel.png")
        img = img.subsample(2)
        self.__canvas.create_image(20, 20, anchor=NW, image=img)
        #self.__canvas.update()

        # Button actions
        self.btn_finish = Button(self, text="finish", width=15, bg='white', command=self.close_window)
        self.btn_finish.pack(side="right", padx=5, pady=5)

        self.btn_show = Button(self, text="show", width=15, bg='white',
                               command=lambda: self.show_gaze_points(window_x, window_y))
        self.btn_show.pack(side="top", padx=5, pady=5)

        print("Avg Pupil sizes: ", self.__pupil_data_list)
        print("Gaze Points ", self.__gaze_data_list)

    def close_window(self):
        self.destroy()

    def show_gaze_points(self, window_x, window_y):
        img = PhotoImage(file="images/Beispiel.png")
        self.__canvas.create_image(0, 0, anchor=NW, image=img)

        print(self.__gaze_data_list[0])

        for i in range(len(self.__gaze_data_list[0])):
            self.__canvas.create_text(self.__gaze_data_list[0][i][0] * window_x, self.__gaze_data_list[0][i][1] * window_y,
                                      text="x")
        print("finished printing")
