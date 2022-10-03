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
import base64
import seaborn as sns
import numpy as np

app = Flask(__name__)
hops: hs.HopsFlask = hs.Hops(app)



@hops.component(
    "/plot20",
    inputs=[
    hs.HopsNumber("X", "X", "description", hs.HopsParamAccess.LIST),
    hs.HopsNumber("Y", "Y", "description", hs.HopsParamAccess.LIST),
    hs.HopsNumber("c", "c", "description", hs.HopsParamAccess.LIST),
    hs.HopsNumber("s", "s", "description", hs.HopsParamAccess.LIST)
    ],
    outputs=[hs.HopsString("base64img")],
)
def BinaryMultiply(x,y,c,s):
    return create_figure(x,y,c,s)


@hops.component(
    "/windspeed5",
    inputs=[hs.HopsString("T")],
    outputs=[hs.HopsString("w")],
)
def getWindSpeed(city):
    return wind(city)


def wind(city):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    city = city+" weather"
    city = city.replace(" ", "+")
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    wind = soup.select('#wob_ws')[0].getText().strip()
    return wind

def create_figure(x,y,c,s):
    # Change color with c and transparency with alpha. 
    # I map the color to the X axis value.
    plt.scatter(x, y, s=s, c=c, cmap="turbo")
     
    # Add titles (main and on axis)
    plt.xlabel("the X axis")
    plt.ylabel("the Y axis")
    plt.title("A colored bubble plot")
    plt.axis('equal')

    # Show the graph
    my_stringIObytes = io.BytesIO() #https://stackoverflow.com/a/38061400/7866788
    plt.savefig(my_stringIObytes, format='jpg', dpi=300)
    my_stringIObytes.seek(0)
    my_base64_jpgData = base64.b64encode(my_stringIObytes.read())
    plt.close()
    return str(my_base64_jpgData)
   
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

