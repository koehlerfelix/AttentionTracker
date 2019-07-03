import plotly.plotly as py
import plotly.graph_objs as go
import plotly.io as pio
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot


class Absence:

    def __init__(self, data):
        # self._data = data
        print('initializing absence chart!')
        x_absent, y_absent, x_watching, y_watching = ([] for i in range(4))

        for i, dp in enumerate(data):
            x_absent.append(i + 1)
            y_absent.append(dp.absent)
            x_watching.append(i + 1)
            y_watching.append(dp.watching)

        trace_absent = go.Bar(
            x=x_absent,  # slide numbers
            y=y_absent,  # times not watching
            name='Time not watching'
        )
        trace_watching = go.Bar(
            x=x_watching,  # slide numbers
            y=y_watching,  # times watching
            nume='Time watching slide'
        )
        self._data = [trace_absent, trace_watching]

        '''
        trace1 = go.Bar(
            x=['giraffes', 'orangutans', 'monkeys'],
            y=[20, 14, 23],
            name='SF Zoo'
        )
        trace2 = go.Bar(
            x=['giraffes', 'orangutans', 'monkeys'],
            y=[12, 18, 29],
            name='LA Zoo'
        )

        data = [trace1, trace2]
        '''
        layout = go.Layout(
            title='Absence / Watching time per slide',
            barmode='stack',
            xaxis={'title': 'slides'},
            yaxis={'title': 'time spend on slide'}
        )

        # plot([go.Scatter(x=[1, 2, 3], y=[3, 1, 6])])
        # plot([go.Figure(data=data, layout=layout)])
        fig = go.Figure(data=self._data, layout=layout)
        plot(fig)
        # static_image_bytes = pio.to_image(fig, format='png')
        # ImageTk.PhotoImage(static_image_bytes)
        # py.iplot(fig, filename='stacked-bar')
