# Site-specific configuration settings for Review Board
# Definitions of these settings can be found at
# http://docs.djangoproject.com/en/dev/ref/settings/

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'reviewboard',
        'USER': 'reviewboard',
        'PASSWORD': 'root123',
        'HOST': 'localhost',
        'PORT': '',
    },
}

TIME_ZONE = 'Africa/Ouagadougou'

# Unique secret key. Don't share this with anybody.
SECRET_KEY = 'sph!jgp0*p7z20wryow+7_n7%v(s1b#*ibvl44b3pp)0#sz2(l'

# Cache backend settings.
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'localhost:11211',
    },
}

# Extra site information.
SITE_ID = 1
SITE_ROOT = '/'
FORCE_SCRIPT_NAME = ''
DEBUG = False
