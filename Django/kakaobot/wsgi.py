<<<<<<< HEAD
"""
WSGI config for kakaobot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os, sys

sys.path.append('/home/ubuntu/Django')
sys.path.append('/home/ubuntu/Django/myvenv/lib/python3.5/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kakaobot.settings")

application = get_wsgi_application()
=======
"""
WSGI config for kakaobot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os, sys

sys.path.append('/home/ubuntu/Django')
sys.path.append('/home/ubuntu/Django/myvenv/lib/python3.5/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kakaobot.settings")

application = get_wsgi_application()
>>>>>>> 80a3e5d78fc4584f3f8af39bfa45bd82241c5975
