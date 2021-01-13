"""
WSGI config for dnac_monitoring project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/usr/local/dnac_app1')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dnac_monitoring.settings')

application = get_wsgi_application()
