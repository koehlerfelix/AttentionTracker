import math
from matplotlib.figure import Figure

def get_time_per_page_diagramm(gaze_data_list):
    xlen = len(gaze_data_list)
    x = range(xlen)
    y = []
    i = 0
    offscreen_time = []
    while i < xlen:
        offscreen_time.append(0)
        time = len(gaze_data_list[i]) / 90
        y.append(time)

        # calculate off screen time
        for gazepoint in gaze_data_list[i]:
            if math.isnan(gazepoint[0]):
                # for every nan + 90th second
                offscreen_time[i] = offscreen_time[i] + (1 / 90)
        offscreen_time[i] = time - offscreen_time[i]
        i += 1
    width = 0.35  # width of the bars

    f = Figure(figsize=(4, 4), dpi=100)
    a = f.add_subplot(111)
    a.bar(x, y, width, color="red", linewidth=1.0)  # gesamtzeit
    a.bar(x, offscreen_time, width, color="blue", linewidth=1.0)  # offscreen
    a.set_ylabel('Time per Slide Rot:gesamt, blau:offscreen')
    a.set_xlabel('Slide')

    print('offscreen time: ', offscreen_time)

    return f

def get_avrg_pupil_size_diagramm(pupil_size_list, avg_pupil_size):
    xlen = len(pupil_size_list)
    x = range(xlen)
    y = []
    for i in range(0, len(pupil_size_list) - 1):
        y.append((pupil_size_list[i] - avg_pupil_size))
    width = 0.35
    f = Figure(figsize=(4, 4), dpi=100)
    a = f.add_subplot(111)
    a.bar(x, y, width, color="blue", linewidth=1.0)
    a.set_ylabel('Average pupil size')
    a.set_xlabel('Slide')

    return f
