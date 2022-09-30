from flask import Flask
from datetime import datetime
import ghhops_server as hs
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
hops: hs.HopsFlask = hs.Hops(app)



@hops.component(
    "/binmult",
    inputs=[hs.HopsNumber("A"), hs.HopsNumber("B")],
    outputs=[hs.HopsNumber("Multiply")],
)
def BinaryMultiply(a: float, b: float):
    return a * b


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


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

