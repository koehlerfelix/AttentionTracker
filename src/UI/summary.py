"""
Manages charts in a grid layout using tkinter.
A 2 x 2 grid offers space for up to 4 charts
"""
import src.chart.absence as absence


class Summary:
    _charts = []
    # define valid chart type references (names like imports)
    _chart_types = ['absence']

    def __init__(self, charts: []):
        for chart in charts:
            if chart in self._chart_types:
                self._charts.append(chart)
            else:
                self.error('unknown chart type "' + chart + '". Is it registered correctly?')

    """Set data for a chart
    chart_type must be set on class initialization.
    """
    def set_data(self, chart_type, data):
        if chart_type in self._charts:
            absence.Absence(data)
        else:
            self.error('unknown chart type "' + chart_type + '".')

    def error(self, msg):
        print('ERROR: ', msg)
