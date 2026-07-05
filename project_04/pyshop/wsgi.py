"""
WSGI (web-server gateway interface) config for pyshop project.
WSGI is the interface between the Django app and the web server.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pyshop.settings')

application = get_wsgi_application()
