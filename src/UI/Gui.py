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
    __gaze_data_lists = [[[]]]
    __pupil_data_lists = [[]]
    __gaze_data_lists_alternative = __gaze_data_lists_alternative = [[(0.17616580426692963, 0.9616665244102478),
                                                                      (0.17312994599342346, 0.9625645279884338),
                                                                      (0.17123974859714508, 0.9627096056938171),
                                                                      (0.1604757159948349, 0.97650545835495),
                                                                      (0.15545116364955902, 0.9772647619247437),
                                                                      (0.13310305774211884, 1.00267493724823),
                                                                      (0.12856921553611755, 0.9946170449256897),
                                                                      (0.12782439589500427, 1.0020710229873657),
                                                                      (0.12689493596553802, 1.0121006965637207),
                                                                      (0.13718219101428986, 1.0077444314956665),
                                                                      (0.13497498631477356, 1.0115565061569214),
                                                                      (0.13619638979434967, 1.014356255531311),
                                                                      (0.12849360704421997, 1.013929009437561),
                                                                      (0.12918303906917572, 1.008519172668457),
                                                                      (0.12405483424663544, 0.9961434006690979),
                                                                      (0.12331100553274155, 1.0044410228729248),
                                                                      (0.12533849477767944, 1.003523588180542),
                                                                      (0.12468674778938293, 1.0127381086349487),
                                                                      (0.12484980374574661, 1.0171887874603271),
                                                                      (0.5502414703369141, 0.4639076590538025),
                                                                      (0.577083945274353, 0.4470086097717285),
                                                                      (0.6087575554847717, 0.42630094289779663),
                                                                      (0.6135833263397217, 0.4270203709602356),
                                                                      (0.6110949516296387, 0.43400734663009644),
                                                                      (0.6122182607650757, 0.44878721237182617),
                                                                      (0.6110880374908447, 0.4374080002307892),
                                                                      (0.611991286277771, 0.4345487356185913),
                                                                      (0.6102235317230225, 0.42465940117836),
                                                                      (0.6081981658935547, 0.44223371148109436),
                                                                      (0.6088234186172485, 0.4439316987991333),
                                                                      (0.6069790124893188, 0.45158565044403076),
                                                                      (0.6095542311668396, 0.44616976380348206),
                                                                      (0.605530858039856, 0.4403834342956543),
                                                                      (0.6096868515014648, 0.4310469925403595),
                                                                      (0.6079671382904053, 0.42918556928634644),
                                                                      (0.6130997538566589, 0.43560242652893066),
                                                                      (0.6082167029380798, 0.44201934337615967),
                                                                      (0.5907450318336487, 0.4394453167915344),
                                                                      (0.5501024127006531, 0.40939366817474365),
                                                                      (0.40761664509773254, 0.3299483358860016),
                                                                      (0.36401382088661194, 0.3040594160556793),
                                                                      (0.34110671281814575, 0.2923586368560791),
                                                                      (0.3161119520664215, 0.2964918315410614),
                                                                      (0.315214067697525, 0.2959057688713074),
                                                                      (0.3142097592353821, 0.2997483015060425),
                                                                      (0.3111080229282379, 0.30440908670425415),
                                                                      (0.30959370732307434, 0.31329235434532166),
                                                                      (0.3078043758869171, 0.30833879113197327),
                                                                      (0.3085789978504181, 0.3048059344291687),
                                                                      (0.30694466829299927, 0.30364692211151123),
                                                                      (0.3067679703235626, 0.3065465986728668),
                                                                      (0.3048669397830963, 0.3068876266479492),
                                                                      (0.308978408575058, 0.2986430823802948),
                                                                      (0.3102836012840271, 0.30279994010925293),
                                                                      (0.3090665936470032, 0.29668837785720825),
                                                                      (0.3067062795162201, 0.2951664924621582),
                                                                      (0.3056221008300781, 0.29050150513648987),
                                                                      (0.30688685178756714, 0.29661086201667786),
                                                                      (0.3080694079399109, 0.2930557131767273),
                                                                      (0.3058526813983917, 0.29608890414237976),
                                                                      (0.26647743582725525, 0.2631818652153015),
                                                                      (0.2337437868118286, 0.24524681270122528),
                                                                      (0.20092488825321198, 0.204448863863945),
                                                                      (0.12384902685880661, 0.12757320702075958),
                                                                      (0.11224587261676788, 0.11203336715698242),
                                                                      (0.10940185189247131, 0.10570088773965836),
                                                                      (0.10859420150518417, 0.10749735683202744),
                                                                      (0.10838232189416885, 0.11507441103458405),
                                                                      (0.10950224846601486, 0.1248440071940422),
                                                                      (0.11094794422388077, 0.12559598684310913),
                                                                      (0.1111808493733406, 0.12303198128938675),
                                                                      (0.10707736015319824, 0.12213940173387527),
                                                                      (0.10860692709684372, 0.1201924979686737),
                                                                      (0.10576634854078293, 0.11903844028711319),
                                                                      (0.10810433328151703, 0.12266247719526291),
                                                                      (0.10326140373945236, 0.12172795832157135),
                                                                      (0.10606284439563751, 0.11760483682155609),
                                                                      (0.10484661161899567, 0.10772160440683365),
                                                                      (0.10974130779504776, 0.11755474656820297),
                                                                      (0.11017685383558273, 0.12355986982584),
                                                                      (0.1095285415649414, 0.1281249076128006),
                                                                      (0.08947977423667908, 0.1076991856098175),
                                                                      (0.08209356665611267, 0.10061469674110413),
                                                                      (0.07533640414476395, 0.09960629791021347),
                                                                      (0.06622936576604843, 0.10706166177988052),
                                                                      (0.06296569854021072, 0.11448978632688522),
                                                                      (0.06214802712202072, 0.11730662733316422),
                                                                      (0.06117575988173485, 0.11526533216238022),
                                                                      (0.06293704360723495, 0.10613203793764114),
                                                                      (0.05068203806877136, 0.09405443072319031),
                                                                      (0.050277452915906906, 0.09928175061941147),
                                                                      (0.045899078249931335, 0.1053820550441742),
                                                                      (0.039934415370225906, 0.1015411764383316),
                                                                      (0.03977338224649429, 0.09675153344869614),
                                                                      (0.04391682147979736, 0.10146937519311905),
                                                                      (0.04671551659703255, 0.09431089460849762),
                                                                      (0.04500430449843407, 0.097495436668396),
                                                                      (0.045184116810560226, 0.09165500849485397),
                                                                      (0.0447755865752697, 0.09398695826530457),
                                                                      (0.04850691929459572, 0.09623198211193085),
                                                                      (0.04655402526259422, 0.0955788716673851),
                                                                      (0.04556078836321831, 0.10028091818094254),
                                                                      (0.04292435199022293, 0.10206115990877151),
                                                                      (0.04347934573888779, 0.09996205568313599),
                                                                      (0.04516343027353287, 0.10207846015691757),
                                                                      (0.04703674465417862, 0.10278996080160141),
                                                                      (0.04545431211590767, 0.10743097960948944),
                                                                      (0.04663653299212456, 0.10853110253810883),
                                                                      (0.045757971704006195, 0.10918115079402924),
                                                                      (0.045676685869693756, 0.11611804366111755),
                                                                      (0.04549264907836914, 0.10733973979949951),
                                                                      (0.04598044604063034, 0.1081046387553215),
                                                                      (0.04702681675553322, 0.10726138949394226),
                                                                      (0.04635853320360184, 0.11903245747089386),
                                                                      (0.046520184725522995, 0.1139545664191246),
                                                                      (0.044920649379491806, 0.1032659113407135),
                                                                      (0.04126987233757973, 0.09213842451572418),
                                                                      (0.042716436088085175, 0.08974087983369827),
                                                                      (0.0457625649869442, 0.09725894033908844),
                                                                      (0.046431586146354675, 0.10354728996753693),
                                                                      (0.043762702494859695, 0.10909808427095413),
                                                                      (0.04148462042212486, 0.1061309203505516),
                                                                      (0.04263266921043396, 0.09744798392057419),
                                                                      (0.040975674986839294, 0.09099533408880234),
                                                                      (0.040135301649570465, 0.08113827556371689),
                                                                      (0.0387364961206913, 0.07516507059335709),
                                                                      (0.037438467144966125, 0.08200192451477051),
                                                                      (0.03435384854674339, 0.08882889896631241),
                                                                      (0.027651585638523102, 0.09168721735477448),
                                                                      (0.030808841809630394, 0.08039911836385727),
                                                                      (0.031435031443834305, 0.07974027842283249),
                                                                      (0.04103022441267967, 0.07346440106630325),
                                                                      (0.03788912296295166, 0.07769673317670822),
                                                                      (0.039027586579322815, 0.07815860211849213),
                                                                      (0.035299137234687805, 0.07487937808036804),
                                                                      (0.033550795167684555, 0.07216502726078033),
                                                                      (0.032604459673166275, 0.07760939002037048),
                                                                      (0.033053189516067505, 0.08665720373392105),
                                                                      (0.03553221374750137, 0.0855652466416359),
                                                                      (0.04044964164495468, 0.07837476581335068),
                                                                      (0.03897954896092415, 0.06889546662569046),
                                                                      (0.040267862379550934, 0.0757351741194725),
                                                                      (0.03838826343417168, 0.07194791734218597),
                                                                      (0.03602002561092377, 0.07343476265668869),
                                                                      (0.03439522162079811, 0.07139348983764648),
                                                                      (0.03132553771138191, 0.08413001149892807),
                                                                      (0.03407685086131096, 0.08665871620178223),
                                                                      (0.03473491221666336, 0.09134744107723236),
                                                                      (0.039624616503715515, 0.08623925596475601),
                                                                      (0.037517305463552475, 0.08753647655248642),
                                                                      (0.03830450028181076, 0.0755220279097557),
                                                                      (0.03910784795880318, 0.06773007661104202),
                                                                      (0.0409996323287487, 0.06905999034643173),
                                                                      (0.03818792104721069, 0.0761006698012352),
                                                                      (0.034295037388801575, 0.09236815571784973),
                                                                      (0.036724794656038284, 0.10517895966768265),
                                                                      (0.04032785817980766, 0.10440216958522797),
                                                                      (0.042230237275362015, 0.096832275390625),
                                                                      (0.044905371963977814, 0.08828426897525787),
                                                                      (0.04322141408920288, 0.0901021733880043),
                                                                      (0.0450788214802742, 0.08886841684579849),
                                                                      (0.038272641599178314, 0.09968381375074387),
                                                                      (0.03697637468576431, 0.10488474369049072),
                                                                      (0.03337717428803444, 0.11528578400611877),
                                                                      (0.03626669570803642, 0.10168268531560898),
                                                                      (0.04216283559799194, 0.09865167737007141),
                                                                      (0.04042840376496315, 0.0901060625910759),
                                                                      (0.044861260801553726, 0.0980304479598999),
                                                                      (0.04102734476327896, 0.09092017263174057),
                                                                      (0.03754078969359398, 0.08886148035526276),
                                                                      (0.03210308775305748, 0.08042114973068237),
                                                                      (0.032795608043670654, 0.08396656811237335),
                                                                      (0.04226945713162422, 0.08898317068815231),
                                                                      (0.049220528453588486, 0.0902666375041008),
                                                                      (0.05219055712223053, 0.09204736351966858),
                                                                      (0.049486640840768814, 0.0864378809928894),
                                                                      (0.04280498996376991, 0.09400168806314468),
                                                                      (0.07640410214662552, 0.35195282101631165),
                                                                      (0.06472419202327728, 0.2508367896080017),
                                                                      (0.04916686564683914, 0.11403277516365051),
                                                                      (0.04455307871103287, 0.11317751556634903)], []]

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
        btn_start = Button(text="Start", width=15, bg='grey',
                           command=lambda: self.start_collecting(btn_stop, btn_start))
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
        next_page_index = self.__pdfViewer.get_next_page_index()

        # reset thread and save gaze data from page
        if next_page_index == 0:
            current_page_index = len(self.__pdfViewer.get_all_pages()) - 1
        else:
            current_page_index = next_page_index - 1
        self.reset_and_save_gaze_data(current_page_index)

        # restart thread
        self.__thread.start()

        self.render_page(next_page_index)

    # view previous page
    def prev_page(self):
        prev_page_index = self.__pdfViewer.get_previous_page_index()

        # reset thread and save gaze data from page
        if prev_page_index == (len(self.__pdfViewer.get_all_pages()) - 1):
            current_page_index = 0
        else:
            current_page_index = prev_page_index + 1

        self.reset_and_save_gaze_data(current_page_index)

        # restart thread
        self.__thread.start()

        self.render_page(prev_page_index)

    def start_collecting(self, btn_stop, btn_start):
        btn_stop.configure(state="normal")
        btn_start.configure(state="disabled")

        if self.__connected:
            self.__thread.start()

    def stop_collecting(self):
        if self.__connected:
            print('stop collecting')

            # save the last gaze data
            next_page_index = self.__pdfViewer.get_next_page_index()
            if next_page_index == 0:
                current_page_index = len(self.__pdfViewer.get_all_pages()) - 1
            else:
                current_page_index = next_page_index - 1
            self.reset_and_save_gaze_data(current_page_index)

        # checking gaze data and open new window
        if (len(self.__gaze_data_lists[1]) != 0):
            self.__window.withdraw()
            self.newWindow = dash.Dashboard(self.__gaze_data_lists)
        else:
            print("No gazedata but u get some")
            self.__window.withdraw()
            self.newWindow = dash.Dashboard(self.__gaze_data_lists_alternative)

    def reset_and_save_gaze_data(self, page_index):
        self.__thread.join(1)
        self.__thread = threading.Thread(target=self.thread_work)
        self.__eye_tracker.stop_collecting()

        self.__gaze_data_lists[page_index].append(eyetracker.get_gaze_data())
        self.__pupil_data_lists[page_index].append(eyetracker.get_pupil_data())

        print('Gaze Data on Page ', page_index + 1, ': ', self.__gaze_data_lists[page_index])

    def scan_pupil_size(self):
        print("start scan")


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

        # setting the gaze array
        for x in range(0, len(self.__pdfViewer.get_all_pages())):
             self.__gaze_data_lists.append([])
             self.__pupil_data_lists.append([])

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

    def compute_avg_pupil_size(self, pupil_list):
        avg_list = []
        for x in range(0, len(pupil_list)):
            avg_list.append(sum(pupil_list[x]))

        return avg_list