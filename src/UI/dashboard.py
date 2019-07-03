import tkinter as tk
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import math


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

        print('pupil list: ', self.__pupil_data_list)

        # Button actions
        self.btn_finish = Button(self, text="finish", width=15, bg='white', command=self.close_window)
        self.btn_finish.pack(side="bottom", padx=5, pady=5)

        #self.show_time_per_page_diagramm()
        f = self.get_time_per_page_diagramm()
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


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

    def get_time_per_page_diagramm(self):
        xlen = len(self.__gaze_data_list)
        x = range(xlen)
        y = []
        i = 0
        offscreen_time = []
        while i < xlen:
            offscreen_time.append(0)
            time = len(self.__gaze_data_list[i]) / 90
            y.append(time)

            # calculate off screen time
            for gazepoint in self.__gaze_data_list[i]:
                if math.isnan(gazepoint[0]):
                    # for every nan + 90th second
                    offscreen_time[i] = offscreen_time[i] + (1/90)
            offscreen_time[i] = time - offscreen_time[i]
            i += 1
        width = 0.35 #width of the bars

        f = Figure(figsize=(4, 4), dpi=100)
        a = f.add_subplot(111)
        a.bar(x, y, width, color="red", linewidth=1.0) #gesamtzeit
        a.bar(x, offscreen_time, width, color="blue", linewidth=1.0) #offscreen
        a.set_ylabel('Time per Slide Rot:gesamt, blau:offscreen')
        a.set_xlabel('Slide')

        print('offscreen time: ', offscreen_time)

        return f