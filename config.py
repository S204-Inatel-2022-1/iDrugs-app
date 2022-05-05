import os

from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)
app.env = os.getenv('ENV')

if app.env == 'dev':
    url = 'http://localhost:'

pharma_engine = url + '8081/idrugs-pharma-engine/'