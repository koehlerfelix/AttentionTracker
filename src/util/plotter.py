import tkinter as tk
from tkinter import *
import threading


class Plotter:

    def __init__(self, root):
        self.__root = root
        self.__current_page = 0
        self.__gaze_pages = []

    def make_canvas(self, image, page, gaze_data):
        __image = image
        __page = page
        __gaze_data = gaze_data

        # init canvas
        canvas = Canvas(self.__root, width=image.width(), height=image.height(),
                        background='white')
        canvas.create_image(0, 0, anchor=NW, image=__image)

        for i in range(len(__gaze_data)):
            x = __gaze_data[i][0] * __page.size[0]
            y = __gaze_data[i][1] * __page.size[1]

            canvas.create_text(x, y, text="x")

        self.__gaze_pages.append(canvas)

    def num_of_pages(self):
        return len(self.__gaze_pages)

    def get_current_page_index(self):
        return self.__current_page

    def pack_next_page(self):
        if len(self.__gaze_pages) < self.__current_page:
            return
        worker = threading.Thread(target=self.unpack_prev_page())
        worker.start()
        worker.join()
        # self.unpack_prev_page()
        self.__gaze_pages[self.__current_page].pack()
        self.__current_page += 1

    def unpack_prev_page(self):
        print('unpack!!', self.__gaze_pages)
        if self.__gaze_pages[self.__current_page - 1]:
            print('thing: ', self.__gaze_pages[self.__current_page])
            self.__gaze_pages[self.__current_page].destroy()
