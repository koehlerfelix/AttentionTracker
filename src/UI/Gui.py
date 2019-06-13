import tobii_research as tr
import src.eyetracker.eyetracker as eyetracker
from tkinter import *
from tkinter import filedialog
import threading
import util.pdfConverter as pdfCon
import util.pdfViewer as pdfViewer


class GUI:
    __page_index = 0

    def __init__(self):
        trackers = tr.find_all_eyetrackers()
        if len(trackers) > 0:
            self.__eye_tracker = eyetracker.EyeTracker(trackers[0])
            self.__connected = True
        else:
            self.__connected = False
        self.__thread = threading.Thread(target=self.thread_work)

    def run(self):

        window = Tk()

        window_x = 1500
        window_y = 750

        window.title("Attention Assistance")
        window.state('zoomed')
        window.geometry("%dx%d+0+0" % (window_x, window_y))

        window.configure(background='#111111')

        frame = Frame(window, borderwidth=1, background='#1E1E1E')
        frame.pack(fill=BOTH, expand=True)

        # pdf (image) files
        pages = pdfViewer

        # init top menu
        menu = Menu(window)
        window.config(menu=menu)

        # init file sub menu
        def importFile():
            file = filedialog.askopenfilename(initialdir='/', title='Select pdf file',
                                              filetypes=[('pdf files', '*.pdf')])
            read_pdf_thread = threading.Thread(target=self.read_pdf(file))
            read_pdf_thread.start()
            # wait for reading process to finish
            read_pdf_thread.join()
            print('thread joined!!')
            self.load_page()

        file_menu = Menu(window)
        menu.add_cascade(label='File', menu=file_menu)
        file_menu.add_command(label='Import', command=importFile)

        help_menu = Menu(window)
        menu.add_cascade(label='Help', menu=help_menu)
        help_menu.add_command(label='About', command=self.showHelp)

        # place canvas for pdf viewer
        canvas_width = window_x - 80
        canvas_height = window_y - 80

        canvas = Canvas(window, width=canvas_width, height=canvas_height)

        # images = pdfCon.convert()

        # img = PhotoImage(file="src/static/img/myPic.png")
        # canvas.create_image(20, 20, anchor=NW, image=img)

        # taking image from the directory and storing the source in a variable
        page1 = PhotoImage(file="images/Beispiel.png")
        page1 = page1.subsample(2, 2)

        page2 = PhotoImage(file="images/Beispiel2.png")
        page2 = page2.subsample(2, 2)

        # displaying the picture using a 'Label' by passing the 'picture' variriable to 'image' parameter
        label = Label(frame, image=page1, width=1300, height=750, background='#1E1E1E')

        # lbl = Label(frame, text="Text", font=("Arial Bold", 20), bg='black', fg='white', width=80, height=20)
        # lbl.plack(expand='True', padx=5, pady=5)

        btn_start = Button(text="Start", width=15, bg='grey', command=self.start_collecting).pack(side="left", padx=5,
                                                                                                  pady=5)
        btn_stop = Button(text="Stop", width=15, bg='grey', command=self.stop_collecting).pack(side="left", padx=5,
                                                                                               pady=5)

        # btn_connect = Button(text="Connect", command=self.connect).pack(side="left", padx=5, pady=5)

        btn_next = Button(text="next Page", width=15, bg='grey', command=lambda: self.next_page(label, page2)).pack(
            side="right", padx=5, pady=5)
        btn_previous = Button(text="previous Page", width=15, bg='grey',
                              command=lambda: self.next_page(label, page1)).pack(side="right", padx=5, pady=5)

        label.pack(expand='True')
        canvas.pack()

        window.mainloop()

    # init file sub menu
    def importFile(self):
        file = filedialog.askopenfilename(initialdir='/', title='Select pdf file',
                                          filetypes=[('pdf files', '*.pdf')])
        read_pdf_thread = threading.Thread(target=self.read_pdf(file))
        read_pdf_thread.start()
        # wait for reading process to finish
        read_pdf_thread.join()
        print('thread joined!!')
        self.load_page()

    # init help sub menu
    def showHelp(self):
        print('I should help but cannot atm')

    def next_page(self, label, page):
        label.config(image=page)

    def start_collecting(self):
        if self.__connected:
            self.__thread.start()

    def stop_collecting(self):
        if self.__connected:
            self.__thread.join(1)
            self.__eye_tracker.stop_collecting()
            print(eyetracker.get_gaze_data())

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

    def read_pdf(self, file):
        pdfViewer.set_pages(pdfCon.convert(file))

    def load_page(self, page=0):
        if page > len(pdfViewer.get_all_pages):
            return
        print('images: ', pdfViewer.get_all_pages)
        print('first img: ', pdfViewer.get_all_pages)
        img = PhotoImage(file="src/static/img/myPic.png")
        self.canvas.create_image(20, 20, anchor=NW, image=img)

    def is_connected(self):
        return self.__connected

    def get_page_index(self):
        return self.__page_index

    def set_page_index(self, newIndex):
        self.__page_index == newIndex

    def increment_page_index(self):
        self.__page_index == self.get_page_index + 1

    def decrement_page_index(self):
        self.__page_index == self.get_page_index - 1
