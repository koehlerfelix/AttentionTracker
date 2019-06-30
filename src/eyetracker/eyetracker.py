import tobii_research as tr

gaze_data_list = []
pupil_data_list = []

def gaze_data_callback(gaze_data):
    # Print gaze points of left and right eye
    # print("Left eye: ({gaze_left_eye}) \t Right eye: ({gaze_right_eye})".format(
    #   gaze_left_eye=gaze_data['left_gaze_point_on_display_area'],
    #    gaze_right_eye=gaze_data['right_gaze_point_on_display_area']))
    global gaze_data_list
    gaze_data_list.append(gaze_data['right_gaze_point_on_display_area'])

    global pupil_data_list
    pupil_data_list.append(gaze_data['right_pupil_diameter'])


def get_pupil_data():
    return pupil_data_list


def get_gaze_data():
    return gaze_data_list


class EyeTracker:

    def __init__(self, tobii_tracker):
        self.__tobii_tracker = tobii_tracker

    def start_collecting(self):
        global gaze_data_list
        global pupil_data_list
        gaze_data_list = []
        pupil_data_list = []
        self.__tobii_tracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)

    def stop_collecting(self):
        self.__tobii_tracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)