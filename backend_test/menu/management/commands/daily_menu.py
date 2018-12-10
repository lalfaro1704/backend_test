from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import translation
from django.utils.translation import ugettext_lazy as _

from backend_test.menu.tasks import daily_menu


class Command(BaseCommand):
    help = _('Notification for daily menu.')

    def handle(self, *args, **options):
        translation.activate('es')  # Spanish locale.

        translation.activate(settings.LANGUAGE_CODE)  # Or something else.

        self.stdout.write(self.style.SUCCESS(daily_menu()))

        translation.deactivate()
