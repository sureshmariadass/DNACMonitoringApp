import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir("C:/Windows/System32/config/systemprofile/AppData/Local/Jenkins/.jenkins/workspace/DNACMonitoring/venv/Lib/site-packages")




# Add the app's directory to the PYTHONPATH
sys.path.append('C:/Windows/System32/config/systemprofile/AppData/Local/Jenkins/.jenkins/workspace/DNACMonitoring')
sys.path.append('C:/Windows/System32/config/systemprofile/AppData/Local/Jenkins/.jenkins/workspace/DNACMonitoring')

os.environ['DJANGO_SETTINGS_MODULE'] = 'dnac_monitoring.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dnac_monitoring.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
