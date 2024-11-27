
from celery.schedules import crontab
from flask import current_app as app
from application.celery.tasks import send_daily_reminder, send_monthly_report

celery_app = app.extensions['celery']



@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(hour=18, minute=30), send_daily_reminder.s(), name='Daily Reminder')

    sender.add_periodic_task(crontab(day_of_month=1,hour=8, minute=0), send_monthly_report.s(), name='Monthly Reminder')
