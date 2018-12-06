# standard library
from datetime import datetime

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
    message = "Menu sent successfully."
    current_day = datetime.now()
    timezones = ['America/Santiago']

    try:
        menu = Menu.objects.filter(
            date__date=current_day.date(),
            is_active=True)  # menu of the day
    except Menu.DoesNotExist:
        message = "Sorry, not menu for today. Italian Complete to everyone!."
        logger.info(message)
        return False, message

    users = slack.api_call("users.list")  # users on my slack space
    url = 'http://localhost:4200/menu/{}'.format(menu.id)
    if users['ok']:
        for user in users['members']:
            if user['tz'] in timezones:
                notification = 'Hi {}! The menu for today in the following link: {}, good appetite.'.format(
                    user['name'], url)
                slack.api_call(
                    "reminders.add",
                    text=notification,
                    user=user['id'],
                    time=current_day.time()
                )

    logger.info(message)

    return True, message
