from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User;

class Command(BaseCommand):

    def handle(self, *args, **options):
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')
        # if Account.objects.count() == 0:
        #     for user in settings.ADMINS:
        #         username = 'admin'
        #         email = 'admin@choozie.com'
        #         password = 'admin'
        #         print('Creating account for %s (%s)' % (username, email))
        #         admin = Account.objects.create_superuser(email=email, username=username, password=password)
        #         admin.is_active = True
        #         admin.is_admin = True
        #         admin.save()
        
