from flask import Flask
from flask import send_file
from flask import send_from_directory
from datetime import datetime
import ghhops_server as hs
import requests
from bs4 import BeautifulSoup

import io
import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

app = Flask(__name__)
hops: hs.HopsFlask = hs.Hops(app)



@hops.component(
    "/plot3",
    inputs=[hs.HopsNumber("A"), hs.HopsNumber("B")],
    outputs=[hs.HopsNumber("Multiply")],
)
def BinaryMultiply(a: float, b: float):
    return graph_visualization()


@hops.component(
    "/windspeed5",
    inputs=[hs.HopsString("T")],
    outputs=[hs.HopsString("w")],
)
def getWindSpeed(city):
    return wind(city)



# def wind(city):
#     headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#     city = city+" weather"
#     city = city.replace(" ", "+")
#     res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
#     soup = BeautifulSoup(res.text, 'html.parser')
#     wind = soup.select('#wob_ws')[0].getText().strip()
#     return wind


# def graph_visualization():
#     fig = create_figure()
#     canvas = FigureCanvas(fig)
#     img = io.BytesIO()
#     fig.savefig(img, format='png')
#     img.seek(0)
#     return send_file(img, mimetype='image/png',as_attachment=True,download_name="file.png")


# # @app.route('/plot.png')
# # def plot_png():
# #     fig = create_figure()
# #     output = io.BytesIO()
# #     #FigureCanvas(fig).print_png(output)
# #     plt.savefig(output, format='png')
# #     return send_file(output, mimetype='image/png', as_attachment=True)
# #     return Response(output.getvalue(), mimetype='image/png')

# def create_figure():
#     fig = Figure()
#     axis = fig.add_subplot(1, 1, 1)
#     xs = range(100)
#     ys = [random.randint(1, 50) for x in xs]
#     axis.plot(xs, ys)
#     return fig

# # @app.route('/plot.png')
# # def plot_png():
# #     fig = create_figure()
# #     #fig.savefig('/some_unique_string2.pdf')
# #     print(hello)
# #     img = io.BytesIO()
# #     plt.savefig(img)
# #     img.seek(0)
# #     #return send_file(img, mimetype='image/png')
# #     send_from_directory('/', 'some_unique_string.png')
# #     #output = io.BytesIO()
# #     #FigureCanvas(fig).print_png(output)
# #     #return send_file()
# #     #return Response(output.getvalue(), mimetype='image/png')

# # def create_figure():
# #     fig = Figure()
# #     axis = fig.add_subplot(1, 1, 1)
# #     xs = range(100)
# #     ys = [random.randint(1, 50) for x in xs]
# #     axis.plot(xs, ys)
# #     fig.savefig('test.png')

# #     return fig



if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

