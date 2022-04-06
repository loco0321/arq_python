from datetime import datetime
from time import sleep

from arq_python2.celery import app


@app.task
def create_movie():
    sleep(10)
    print('time:', datetime.now())
