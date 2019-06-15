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
        self.geometry("%dx%d+0+0" % (window_x-100, window_y-100))

        self.configure(background='#111111')

        frame = Frame(self, borderwidth=1, background='#1E1E1E')
        frame.pack(fill=BOTH, expand=True)

        self.__label = Label(frame, width=window_x - 200, height=window_y - 200, background='white')

        self.__label.pack(expand='True')

        self.btn_finish = Button(self, text="finish", width=15, bg='white', command=self.close_window)
        self.btn_finish.pack(side="top", padx=5, pady=5)




    def close_window(self):
        self.destroy()