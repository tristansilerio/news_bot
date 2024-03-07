#scheduler.py
from apscheduler.schedulers.blocking import BlockingScheduler
from main import my_function
sched = BlockingScheduler()

@sched.scheduled_job('cron', hour=8)
def scheduled_job():
    print('This job is run every day at 8 AM.')
    my_function()

sched.start()