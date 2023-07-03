from flask import Flask, render_template
import plotly
from plotly.graph_objs import Scatter, Layout
import json

app = Flask(__name__)


@app.route('/')
def index():

    data = Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])
    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('dashboard_test.html', plot=graphJSON)

if __name__ == '__main__':
    app.run()
