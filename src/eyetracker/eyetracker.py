import tobii_research as tr

class Eyetracker:

    def __init__(self,tobii_tracker):
        self.__tobii_tracker = tobii_tracker

    def gaze_data_callback(gaze_data):
        # Print gaze points of left and right eye
        print("Left eye: ({gaze_left_eye}) \t Right eye: ({gaze_right_eye})".format(
            gaze_left_eye=gaze_data['left_gaze_point_on_display_area'],
            gaze_right_eye=gaze_data['right_gaze_point_on_display_area']))

    def start_collecting(self):
        self.__tobii_tracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, self.gaze_data_callback, as_dictionary=True)

    def stop_collecting(self):
        self.__tobii_tracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, self.gaze_data_callback)
