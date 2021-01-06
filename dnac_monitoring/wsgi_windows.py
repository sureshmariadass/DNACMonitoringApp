import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir("C:/Users/Administrator/Desktop/dnac_monitoring/venv/Lib/site-packages")




# Add the app's directory to the PYTHONPATH
sys.path.append('C:/Users/Administrator/Desktop/dnac_monitoring')
sys.path.append('C:/Users/Administrator/Desktop/dnac_monitoring')

os.environ['DJANGO_SETTINGS_MODULE'] = 'dnac_monitoring.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dnac_monitoring.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
