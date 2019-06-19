import tkinter as tk
from tkinter import *


class Plotter:

    def __init__(self, frame):
        self.__frame = frame
        self.__gaze_pages = []

    def make_canvas(self, image, page, gaze_data):
        __image = image
        __page = page
        __gaze_data = gaze_data

        # create frame
        # frame = Frame(self, borderwidth=1, background='#1E1E1E')
        # frame.pack(fill=BOTH, expand=True)

        # make canvas
        # canvas = Canvas(frame, width=__page - 130, height=window_y - 230, background='white')
        canvas = Canvas(self.__frame, width=__page.size[0], height=__page.size[1], background='white')
        # canvas.pack(expand='True')

        # loding image into canvas !!!!not working!!!! and i have no clue why
        # img = PhotoImage(file="images/Beispiel.png")
        # img = img.subsample(2)
        # canvas.create_image(0, 0, anchor=NW, image=page_cache[0])
        print(__page)
        canvas.create_image(0, 0, anchor=NW, image=__image)

        # get dimensions of canvas
        # self.canvas_rootx = canvas.winfo_rootx()
        # self.canvas_rooty = canvas.winfo_rooty()
        # self.canvas_width = canvas.winfo_width()
        # self.canvas_height = canvas.winfo_height()

        # Button actions
        # self.btn_finish = Button(self, text="finish", width=15, bg='white', command=self.close_window)
        # self.btn_finish.pack(side="right", padx=5, pady=5)

        # self.btn_show = Button(self, text="show", width=15, bg='white',
                               # command=lambda: self.show_gaze_points(canvas, window_x, window_y))
        # self.btn_show.pack(side="top", padx=5, pady=5)

        for i in range(len(__gaze_data)):
            x = __gaze_data[i][0] * __page.size[0]
            y = __gaze_data[i][1] * __page.size[1]

            # if (x < self.canvas_rootx) or (x > self.canvas_rootx + self.canvas_width) or (y < self.canvas_rooty) or (y > self.canvas_rooty + self.canvas_height):
            #    continue
            # else:
            canvas.create_text(x, y, text="x")

        self.__gaze_pages.append(canvas)

    def show_gaze_points(self, canvas, window_x, window_y):
        img = PhotoImage(file="images/Beispiel.png")
        canvas.create_image(0, 0, anchor=NW, image=img)

        for i in range(len(self.__gaze_data_list)):
            x = self.__gaze_data_list[i][0] * window_x
            y = self.__gaze_data_list[i][1] * window_y

            # if (x < self.canvas_rootx) or (x > self.canvas_rootx + self.canvas_width) or (y < self.canvas_rooty) or (y > self.canvas_rooty + self.canvas_height):
            #    continue
            # else:
            canvas.create_text(x, y, text="x")

        print("finished printing")

    def get_gaze_page(self, index):
        if len(self.__gaze_pages) < index:
            return
        return self.__gaze_pages[index]
