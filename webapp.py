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

# @app.route('/')
# def homepage():
#     the_time = "Anne ist lieb"

#     return 

#     <h1>Hello heroku</h1>
#     <p>It is currently {time}.</p>

#     <img src="http://loremflickr.com/600/600" />

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

