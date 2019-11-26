from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')

app = Celery('Celery')

app.autodiscover_tasks()

app.conf.timezone = 'America/Recife'

app.conf.beat_schedule = {
    'run_every_day': {
        'task': 'celery_tasks.tasks.load_cards',
        'schedule': crontab(hour = 3, minute = 00)
    }
}