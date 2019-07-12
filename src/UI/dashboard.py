import tkinter as tk
from tkinter import *
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import src.UI.diagramms as diagramms


class Dashboard(tk.Toplevel):

    # gaze data list hat 2 listen: [0] hat keine "NaN" werte [1] hat welche

    def __init__(self, gaze_data_list, avg_pupil_size, pupil_data_list, statistics):
        self.__gaze_data_list = gaze_data_list
        self.__pupil_data_list = pupil_data_list
        self.__avg_pupil_size = avg_pupil_size
        statistics = statistics

        tk.Toplevel.__init__(self)

        window_x = self.winfo_screenwidth()
        window_y = self.winfo_screenheight()

        self.title('Attention Assistance Results')
        self.state('zoomed')
        self.geometry("%dx%d+0+0" % (window_x - 100, window_y - 100))

        self.configure(bg='#111111')

        # create grid frames
        top_frame = Frame(self, bg='#e8e6e6')
        top_frame.pack(fill=X)

        chart_frame = Frame(self, bg='#878787')
        chart_frame.pack(fill=BOTH, expand=True)

        button_frame = Frame(self, bg='#636363')
        button_frame.pack(fill=X, side=BOTTOM)

        # heading and general information
        view_time = statistics['end_time'] - statistics['start_time']
        top_summary = Text(top_frame, height=20, width=window_x, bg='#e8e6e6', bd=0)
        top_summary.tag_configure('heading', font=('Verdana', 20, 'bold'))
        top_summary.tag_configure('alert', foreground='#d90000')
        top_summary.insert(END, '\nAttention Summary\n', 'heading')
        top_summary.insert(END, 'Overall time spent: ' + str(view_time) + '\n')
        # top_summary.insert(END, 'Seems like attention is decreasing: \n')
        top_summary.insert(END, 'Shortest view time: ' + str(min(statistics['page_times'])) + ' seconds on page X\n')
        top_summary.insert(END, 'Longest view time: ' + str(max(statistics['page_times'])) + ' seconds on page X\n')
        # top_summary.insert(END, 'Average view time: ' + str(max(statistics['page_times'])) + ' seconds on page X\n')
        top_summary.config(state=DISABLED)
        top_summary.pack(side=TOP, padx=20)

        print('pupil list: ', self.__pupil_data_list)

        # Button actions
        self.btn_finish = Button(button_frame, text="finish", width=15, bg='white', command=self.close_window)
        self.btn_finish.pack(side="bottom", padx=5, pady=5)

        time_diagramm = diagramms.get_time_per_page_diagramm(self.__gaze_data_list)
        canvas = FigureCanvasTkAgg(time_diagramm, chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        canvas._tkcanvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        pupil_diagramm = diagramms.get_avg_pupil_size_diagramm(self.__pupil_data_list, self.__avg_pupil_size)
        canvas = FigureCanvasTkAgg(pupil_diagramm, chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        canvas._tkcanvas.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def close_window(self):
        self.destroy()

    def show_gaze_points(self, window_x, window_y):
        img = PhotoImage(file="images/Beispiel.png")
        self.__canvas.create_image(0, 0, anchor=NW, image=img)

        print(self.__gaze_data_list[0])

        for i in range(len(self.__gaze_data_list[0])):
            self.__canvas.create_text(self.__gaze_data_list[0][i][0] * window_x,
                                      self.__gaze_data_list[0][i][1] * window_y,
                                      text="x")
        print("finished printing")
