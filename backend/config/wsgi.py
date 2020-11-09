import os

from django.core.wsgi import get_wsgi_application
# from whitenoise.django import DjangoWhiteNoise


# This will set production as default, but we must still set it with an
# ENV on heroku to ensure that the migrate command runs agains the correct DB
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
# application = DjangoWhiteNoise(application)
