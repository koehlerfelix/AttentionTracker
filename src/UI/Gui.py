import tobii_research as tr
import eyetracker.eyetracker as eyetracker
from tkinter import *
from tkinter import filedialog
import threading
import util.pdfViewer as pdfV
import src.UI.dashboard as dash
from PIL import ImageTk


class GUI:
    __pdfViewer = pdfV.PdfViewer()
    __page_cache = dict()  # provide 'fast render' in case page has been rendered before

    def __init__(self):
        trackers = tr.find_all_eyetrackers()

        if len(trackers) > 0:
            self.__eye_tracker = eyetracker.EyeTracker(trackers[0])
            self.__connected = True
        else:
            self.__connected = False
        self.__thread = threading.Thread(target=self.thread_work)

        # set window reference
        self.__window = Tk()

        # set label reference
        self.__label = Label()

        # set interaction items reference
        self.__pdf_nav_items = dict()
        self.__eye_tracker_con_items = dict()

        # set page counter
        self.__page_counter = StringVar()
        self.__page_counter.set('1 / 1')

    def run(self):

        window_x = self.__window.winfo_screenwidth()
        window_y = self.__window.winfo_screenheight()

        self.__window.title('Attention Assistance')
        self.__window.state('zoomed')
        self.__window.geometry("%dx%d+0+0" % (window_x, window_y))

        self.__window.configure(background='#111111')

        # init top menu
        menu = Menu(self.__window)
        self.__window.config(menu=menu)

        file_menu = Menu(self.__window)
        menu.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='Import', command=self.import_file)

        help_menu = Menu(self.__window)
        menu.add_cascade(label='Help', menu=help_menu)
        help_menu.add_command(label='About', command=self.show_help)

        frame = Frame(self.__window, borderwidth=1, background='#1E1E1E')
        frame.pack(fill=BOTH, expand=True)

        # set starting page
        starting_page = PhotoImage(file="static/img/default.png")
        starting_page = starting_page.subsample(2, 2)
        self.__label = Label(frame, image=starting_page,
                             width=window_x - 200,
                             height=window_y - 200,
                             background='#1E1E1E')

        # lbl = Label(frame, text="Text", font=("Arial Bold", 20), bg='black', fg='white', width=80, height=20)
        # lbl.plack(expand='True', padx=5, pady=5)

        # init eye-tracking buttons
        btn_start = Button(text="Start", width=15, bg='grey', command=lambda: self.start_collecting(btn_stop))
        self.__eye_tracker_con_items['btn_start'] = btn_start
        btn_start.pack(side="left", padx=5, pady=5)

        btn_stop = Button(text="Stop", width=15, bg='grey', state="disabled", command=self.stop_collecting)
        self.__eye_tracker_con_items['btn_stop'] = btn_stop
        btn_stop.pack(side="left", padx=5, pady=5)

        # btn_connect = Button(text="Connect", command=self.connect).pack(side="left", padx=5, pady=5)

        # init pdf navigation buttons
        btn_next = Button(text="Next", width=15, bg='grey', state=DISABLED,
                          command=lambda: self.next_page())
        self.__pdf_nav_items['btn_next'] = btn_next
        btn_next.pack(side="right", padx=5, pady=5)

        btn_prev = Button(text="Previous", width=15, bg='grey', state=DISABLED,
                          command=lambda: self.prev_page())
        self.__pdf_nav_items['btn_prev'] = btn_prev
        btn_prev.pack(side="right", padx=5, pady=5)

        # init page counter
        my_label = Label(frame, textvariable=self.__page_counter, fg='#f2f2f2', bg='#1E1E1E',
                         font='Verdana 10 bold', justify=CENTER) \
            .pack(side=BOTTOM)

        self.__label.pack(expand='True')

        self.__window.mainloop()

    # init help sub menu
    def show_help(self):
        print('I should help but cannot atm..........send help pls')

    # view next page
    def next_page(self):
        self.render_page(self.__pdfViewer.get_next_page_index())

    # view previous page
    def prev_page(self):
        self.render_page(self.__pdfViewer.get_previous_page_index())

    def start_collecting(self, btn_stop):
        btn_stop.configure(state="active")
        if self.__connected:
            self.__thread.start()

    def stop_collecting(self):
        if self.__connected:
            self.__thread.join(1)
            self.__eye_tracker.stop_collecting()
            print(eyetracker.get_gaze_data())

        # checking gaze data and open new window
        __gaze_data_list = eyetracker.get_gaze_data()
        if __gaze_data_list.__sizeof__() > 0:
            self.__window.withdraw()
            self.newWindow = dash.Dashboard(__gaze_data_list)
        else:
            print("Error no gazedata")

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

    def import_file(self):
        file = filedialog.askopenfilename(initialdir='/', title='Select pdf file',
                                          filetypes=[('pdf files', '*.pdf')])
        read_pdf_thread = threading.Thread(target=self.read_pdf(file))
        read_pdf_thread.start()

        # wait for reading process to finish
        read_pdf_thread.join()
        self.render_page()

        # activate nav buttons
        for key, value in self.__pdf_nav_items.items():
            value.configure(state=NORMAL)

    def read_pdf(self, file):
        if bool(self.__page_cache):
            self.__page_cache = dict()
        self.__pdfViewer.init_file(file)

    def render_page(self, page_index=0):
        if page_index in self.__page_cache:
            loaded_page = self.__page_cache[page_index]

        else:
            loaded_page = self.__pdfViewer.get_page(page_index)

            # compute resize dimensions
            l_dim = {'width': self.__label.winfo_width(), 'height': self.__label.winfo_height()}
            resize = 1  # resize factor
            if loaded_page.size[0] > l_dim['width']:  # page width > label width
                resize = l_dim['width'] / loaded_page.size[0]

            if loaded_page.size[1] * resize > l_dim['height']:  # page height * resize factor > label height
                resize = l_dim['height'] / loaded_page.size[1]

            if resize < 1:
                loaded_page = loaded_page.resize((int(loaded_page.size[0] * resize), int(loaded_page.size[1] * resize)))

            loaded_page = ImageTk.PhotoImage(loaded_page)
            # save loaded page in cache
            self.__page_cache[page_index] = loaded_page

        # put new page into label
        self.__label.configure(image=loaded_page)
        self.__label.image = loaded_page

        # set current page state
        self.__pdfViewer.set_page_index(page_index)

        # update page counter
        self.__page_counter.set(' '.join([str(page_index + 1), '/', str(self.__pdfViewer.num_of_pages())]))

    def is_connected(self):
        return self.__connected
