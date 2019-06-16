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


        # create frame
        frame = Frame(self, borderwidth=1, background='#1E1E1E')
        frame.pack(fill=BOTH, expand=True)

        # making canvas
        self.__canvas = Canvas(frame, width=window_x - 130, height=window_y - 230, background='white')
        self.__canvas.pack(expand='True')
        self.__canvas.update()

        img = PhotoImage(file="images/Beispiel.png")
        self.__canvas.create_image(20, 20, anchor=NW, image = img)
        self.__canvas.update()
        # self.__label = Label(frame, width=220, height=45, background='white')
        # self.__label.pack(expand='True')



        # Button actions
        self.btn_finish = Button(self, text="finish", width=15, bg='white', command=self.close_window)
        self.btn_finish.pack(side="right", padx=5, pady=5)

        self.btn_show = Button(self, text="show", width=15, bg='white',
                               command=lambda: self.show_gaze_points(window_x, window_y))
        self.btn_show.pack(side="top", padx=5, pady=5)


    def close_window(self):
        self.destroy()


    def show_gaze_points(self, window_x, window_y):

        img = PhotoImage(file="images/Beispiel.png")
        img = img.subsample(2)
        self.__canvas.create_image(0, 0, anchor=NW, image=img)

        for i in range(self.__gaze_data_list.__sizeof__()):
            self.__canvas.create_text(self.__gaze_data_list[i][0] * window_x, self.__gaze_data_list[i][1] * window_y, text="x")
            self.__canvas.update
        print("finished printing")