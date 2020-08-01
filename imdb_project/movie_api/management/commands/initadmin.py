 
import logging

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from imdb.settings import ADMIN_USERNAME, ADMIN_EMAIL, ADMIN_PASSWORD

class Command(BaseCommand):
    help = 'Create superuser account'
    
    logger = logging.getLogger(__name__)

    def handle(self, *args, **options):
        if User.objects.filter(email=ADMIN_EMAIL).count() == 0:
            admin = User.objects.create_superuser(email=ADMIN_EMAIL, username=ADMIN_USERNAME, password=ADMIN_PASSWORD)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
            msg = 'Admin User - {} created'.format(ADMIN_USERNAME)
            self.logger.debug(msg)    
            self.stdout.write(self.style.SUCCESS(msg))
        else:
            err_msg = 'Admin user already exist'
            self.logger.debug(err_msg)    
            self.stdout.write(err_msg)
