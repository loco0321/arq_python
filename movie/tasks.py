from datetime import datetime
from time import sleep

import requests

from arq_python2.celery import app
from movie.models import Currency
from bs4 import BeautifulSoup


@app.task
def create_movie(a, b):
    print(f'{a} - {b}')
    sleep(20)
    print(f'time: {datetime.now()}')


@app.task
def create_currency_value():
    code = 'EUR'
    url = 'https://www.google.com/search'
    params = {'q': f'1 usd to {code}'}
    response = requests.get(url, params=params)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    element = soup.select_one('.BNeawe.iBp4i.AP7Wnd')

    str_value, *_ = element.text.split(' ')
    value = float(str_value.replace(',', ''))

    currency = Currency.objects.create(code=code, value=value)
    return str(currency)
