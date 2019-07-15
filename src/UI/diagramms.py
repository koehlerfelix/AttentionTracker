import math
from matplotlib.figure import Figure


def get_time_per_page_diagram(gaze_data_list):
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
    a.bar(x, y, width, color="blue", linewidth=1.0, label="offscreen")  # gesamtzeit
    a.bar(x, offscreen_time, width, color="green", linewidth=1.0, label="onscreen")  # offscreen
    a.legend(loc='upper right')
    a.set_ylabel('Time per Slide')
    a.set_xlabel('Slide')

    print('offscreen time: ', offscreen_time)

    return f


def get_avg_pupil_size_diagram(pupil_size_list, avg_pupil_size):
    xlen = len(pupil_size_list)
    x = range(xlen)
    y = []
    for i in range(0, len(pupil_size_list)):
        y.append(((pupil_size_list[i] / avg_pupil_size) - 1) * 100)
    width = 0.35
    f = Figure(figsize=(4, 4), dpi=100)
    a = f.add_subplot(111)
    a.bar(x, y, width, color="blue", linewidth=1.0)
    a.set_ylabel('deviation of average pupil size in %')
    a.set_xlabel('Slide')

    return f


def get_statistics(gaze_data):
    num_of_pages = len(gaze_data)

    # statistical information
    statistic = {'view_time': 0,  # overall view time of pdf
                 'page_times': []}  # for each page (key = page number): start_time and end_time

    for page in range(num_of_pages):
        page_time = len(gaze_data[page]) / 90
        statistic['page_times'].append(page_time)
        statistic['view_time'] = statistic['view_time'] + page_time
    print('timings: ', statistic)

    return statistic


def get_avg_pupil_size_diagram2(pupil_size_list, avg_pupil_size):
    xlen = len(pupil_size_list)
    x = range(xlen)
    y = []
    for i in range(0, len(pupil_size_list)):
        y.append(((pupil_size_list[i] / avg_pupil_size) - 1) * 100)
    width = 0.35
    f = Figure(figsize=(4, 4), dpi=100)
    a = f.add_subplot(111)
    a.plot(x, y, width, color="blue", linewidth=1.0)
    a.set_ylabel('deviation of average pupil size in %')
    a.set_xlabel('Slide')

    return f
