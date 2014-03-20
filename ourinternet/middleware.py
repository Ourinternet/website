# - * - Coding: utf-8 - * -
from django.conf import settings

CONTENT_TYPES = ('text/html', 'application/xhtml+xml', 'application/xml')
X_UA_VALUES = getattr(settings,  'X_UA_COMPATIBLE',  None)


class XUACompatibleMiddleWare (object):
    """
    Adds a header X-UA-Compatible
    Allows compatibility HTML5
    """
    def process_response(self,  request,  response):
        response_content_type = response.get('Content-Type', '').split(';', 1)[0].lower()
        if response_content_type in CONTENT_TYPES:
            if not 'X-UA-Compatible' in response and X_UA_VALUES:
                response['X-UA-Compatible'] = ','.join(map(lambda key: '%s=%s' % (key, X_UA_VALUES[key]), X_UA_VALUES))
        return  response