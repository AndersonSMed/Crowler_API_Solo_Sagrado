from celery import app
from bs4 import BeautifulSoup

import requests

@app.task
def load_cards():
    pass