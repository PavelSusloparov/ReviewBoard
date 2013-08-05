import os
import sys 
import site 

site.addsitedir('/root/envs/reviewboard/lib/python2.6/site-packages')
sys.path.append('/var/www/reviewboard/conf')
sys.path.append('/usr/lib/python2.6/site-packages/ReviewBoard-1.6.13-py2.6.egg/reviewboard')
#sys.path.append('/root/envs/reviewboard/lib/python2.6/site-packages/ReviewBoard-1.7.6-py2.6.egg/reviewboard')
#sys.path.append('/root/envs/reviewboard/lib/python2.6/site-packages/Django-1.4.5-py2.6.egg/django')
sys.path.append('/usr/lib/python2.6/site-packages/Django-1.3.3-py2.6.egg/django')
#sys.path.append('/root/envs/reviewboard/lib/python2.6/site-packages/django')

#sys.path.append('/usr/lib/python2.6/site-packages/ReviewBoard-1.7.6-py2.6.egg/reviewboard')
#sys.path.append('/usr/lib/python2.6/site-packages/django')

os.environ['DJANGO_SETTINGS_MODULE'] = "reviewboard.settings"
os.environ['PYTHON_EGG_CACHE'] = "/var/www/reviewboard/tmp/egg_cache"
os.environ['HOME'] = "/var/www/reviewboard/data"

#sys.path = sys.path + ['/var/www/reviewboard/conf',]
#sys.path = sys.path + ['/root/envs/reviewboard/lib/python2.6/site-packages/',]
#sys.path = sys.path + ['/root/envs/reviewboard/lib/python2.6/site-packages/Django-1.3.3-py2.6.egg/django/',]

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
