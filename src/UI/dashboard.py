import tkinter as tk
from tkinter import *


class Dashboard(tk.Toplevel):

    def __init__(self, gaze_data_list, page_cache):
        self.__page_cache = page_cache
        self.__gaze_data_list = gaze_data_list

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
        canvas = Canvas(frame, width=window_x - 130, height=window_y - 230, background='white')
        canvas.pack(expand='True')

        # loding image into canvas !!!!not working!!!! and i have no clue why
        img = PhotoImage(file="images/Beispiel.png")
        img = img.subsample(2)
        canvas.create_image(0, 0, anchor=NW, image=img)

        # get dimensions of canvas
        self.canvas_rootx = canvas.winfo_rootx()
        self.canvas_rooty = canvas.winfo_rooty()
        self.canvas_width = canvas.winfo_width()
        self.canvas_height = canvas.winfo_height()

        # Button actions
        self.btn_finish = Button(self, text="finish", width=15, bg='white', command=self.close_window)
        self.btn_finish.pack(side="right", padx=5, pady=5)

        self.btn_show = Button(self, text="show", width=15, bg='white',
                               command=lambda: self.show_gaze_points(canvas, window_x, window_y))
        self.btn_show.pack(side="top", padx=5, pady=5)

    def close_window(self):
        self.destroy()

    def show_gaze_points(self, canvas, window_x, window_y):
        img = PhotoImage(file="images/Beispiel.png")
        canvas.create_image(0, 0, anchor=NW, image=img)

        for i in range(len(self.__gaze_data_list)):
            x = self.__gaze_data_list[i][0] * window_x
            y = self.__gaze_data_list[i][1] * window_y

            #if (x < self.canvas_rootx) or (x > self.canvas_rootx + self.canvas_width) or (y < self.canvas_rooty) or (y > self.canvas_rooty + self.canvas_height):
            #    continue
            #else:
            canvas.create_text(x, y, text="x")

        print("finished printing")
