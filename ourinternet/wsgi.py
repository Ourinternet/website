import os
import sys

sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ourinternet.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()