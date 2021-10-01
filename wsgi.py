# DJANGO passenger_wsgi.py template
import sys, os
from django.core.wsgi import get_wsgi_application


## Project Path
path = '/home/example.com/django_project' ### Path to source files, relative to cPanel directory.

if path not in sys.path:
    sys.path.append(path)

## Optional debug statement.
# print("PATH IS:" + str(sys.path))

## Set the enviromental variables to configure WSGI.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'site_core.settings')

## Declate WSGI as the application to run.
application = get_wsgi_application()
