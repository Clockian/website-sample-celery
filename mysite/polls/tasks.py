from celery import Celery

app = Celery('tasks', backend="rpc://", broker='pyamqp://guest@localhost//')
#app = Celery('tasks')
#app = Celery('tasks', backend='rpc://', broker='pyamqp://')


@app.task
def add(x, y):
    return x + y
