import os

from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)
app.env = os.getenv('ENV')

if app.env == 'dev':
    url = 'https://idrugs-pharma-engine.herokuapp.com'

pharma_engine = url + '/idrugs-pharma-engine'