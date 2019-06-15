import tkinter as tk
from tkinter import *


class Dashboard(tk.Toplevel):

    def __init__(self, __gaze_data_list):
        self.__gaze_data_list = __gaze_data_list

        tk.Toplevel.__init__(self)

        window_x = self.winfo_screenwidth()
        window_y = self.winfo_screenheight()

        self.title('Attention Assistance Results')
        self.state('zoomed')
        self.geometry("%dx%d+0+0" % (window_x - 100, window_y - 100))

        self.configure(background='#111111')

        frame = Frame(self, borderwidth=1, background='#1E1E1E')
        frame.pack(fill=BOTH, expand=True)

        # drawing circles
        self.__canvas = Canvas(frame, width=window_x - 30, height=window_y - 130, background='white')

        self.__label = Label(frame, width=220, height=45, background='white')

        # self.__label.pack(expand='True')

        self.btn_finish = Button(self, text="finish", width=15, bg='white', command=self.close_window)
        self.btn_finish.pack(side="right", padx=5, pady=5)

        self.btn_show = Button(self, text="show", width=15, bg='white',
                               command=lambda: self.show_circles(self.__canvas, window_x, window_y))
        self.btn_show.pack(side="top", padx=5, pady=5)

        self.__canvas.pack(expand='True')

    def close_window(self):
        self.destroy()

    def show_circles(self, canvas, window_x, window_y):
        for i in range(self.__gaze_data_list.__sizeof__()):
            canvas.create_text(self.__gaze_data_list[i][0] * window_x, self.__gaze_data_list[i][1] * window_y, text="x")
            canvas.update

        print("finished printing")
