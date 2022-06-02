import os

from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)
app.env = os.getenv('ENV')

pharma_engine = 'https://idrugs-pharma-engine.herokuapp.com/idrugs-pharma-engine/'
client_engine = 'https://idrugs-client-engine.herokuapp.com/idrugs-client-engine/'