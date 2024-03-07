#main.py

import email_utils
import data

def my_function():
    news_headlines = data.get_latest_headlines()
    print("Got the headlines", news_headlines)
    body = "\n".join([headline["title"] for headline in news_headlines[:5]])
    subject = "Top 5 News Headlines"
    attachments = None
    print("Subject: ", subject)
    print("Body: ", body)
    print("Attachments: ", attachments)
    email_utils.send_email(subject, body, attachments)

if __name__ == '__main__':
    my_function()
    from scheduler import sched
    sched.print_jobs()
    sched.start()