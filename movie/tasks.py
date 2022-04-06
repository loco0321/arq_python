from datetime import datetime
from time import sleep

from arq_python2.celery import app


@app.task
def create_movie(a, b):
    print(f'{a} - {b}')
    sleep(20)
    print(f'time: {datetime.now()}')
