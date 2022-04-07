from datetime import datetime
from time import sleep

from arq_python2.celery import app
from movie.models import Currency


@app.task
def create_movie(a, b):
    print(f'{a} - {b}')
    sleep(20)
    print(f'time: {datetime.now()}')


@app.task
def create_currency_value():
    currency = Currency.objects.create(code='COP', value=3700)
    return str(currency)
