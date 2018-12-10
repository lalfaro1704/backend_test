# standard library
from datetime import datetime
from datetime import timedelta
import time

# Django
from django.conf import settings

# 3rd party library
from celery.decorators import task
from celery.utils.log import get_task_logger
from slackclient import SlackClient

# my models here
from .models import Menu


logger = get_task_logger(__name__)


@task(name="daily_menu")
def daily_menu():
    """
    Slack notification about daily menu.
    """
    slack = SlackClient(settings.SLACK_TOKEN)  # API slack
    message = "Menu sent: {}, not sent: {}."
    current_day = datetime.now()
    timezones = ['America/Santiago']
    sent = 0
    no_sent = 0

    try:
        menu = Menu.objects.get(
            date__date=current_day.date(),
            is_active=True)  # menu of the day
    except Menu.DoesNotExist:
        message = "Sorry, not menu for today. Italian Complete to everyone!."
        logger.info(message)
        return message

    users = slack.api_call("users.list")  # users on my slack workspace
    url = 'http://localhost:4200/menu/{}'.format(menu.id)

    if users['ok']:
        for user in users['members']:
            tz = user.get('tz', None)
            if tz and tz in timezones:
                dts = datetime.now() + timedelta(minutes=1)
                notification = 'Hi {}! The menu for today in the following link: {}, good appetite.'.format(
                    user['name'], url)
                response = slack.api_call(
                    "reminders.add",
                    text=notification,
                    user=user['id'],
                    time=round(dts.timestamp())
                )

                if response["ok"]:
                    sent += 1
                else:
                    no_sent += 1

    logger.info(message.format(sent, no_sent))

    return message.format(sent, no_sent)
