#scheduler.py
from apscheduler.schedulers.blocking import BlockingScheduler
from main import my_function
sched = BlockingScheduler()

@sched.scheduled_job('interval', hours=1)
def scheduled_job():
    print('This job is run every hour.')
    my_function()

sched.start()