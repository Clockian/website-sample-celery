'''from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

#app = Celery('mysite')

app = Celery('mysite',
             broker='amqp://',
             include=['mysite.tasks'])


app.conf.update(
    CELERY_RESULT_BACKEND='amqp'
)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))'''

from __future__ import absolute_import, unicode_literals
from celery import Celery
from django.apps import apps
#from django.conf import settings

app = Celery('mysite',
             broker='pyamqp://',
             backend='rpc://',
             include=['polls.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

#app.config_from_object(settings)
app.autodiscover_tasks()#lambda: [n.name for n in apps.get_app_configs()])

if __name__ == '__main__':
    app.start()
