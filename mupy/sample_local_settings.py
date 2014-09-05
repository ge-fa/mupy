import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.join(BASE_DIR, 'mupy')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

SECRET_KEY = ''

ADMINS = (
    ('example', 'foo@example.org'),
)

DEFAULT_FROM_EMAIL = 'foo@bar.com'

# db connection info
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'mupy.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# handle media and static files serving
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

TIME_ZONE = 'Europe/Athens'


CACHE_BACKEND = ''

# how many days should we keep data in the db
DATA_EXPIRES = '2'

MUNIN_NODES = (
    (
        1, {
            'name': 'main',
            'url': 'http://asd.example.org',
            'cgi_path': 'cgi-bin/munin-cgi-graph/',
            'image_path': ''
        }
    ),
    (
        2, {
            'name': 'extra',
            'url': 'http://extra.example.org',
            'cgi_path': 'cgi-bin/munin-cgi-graph/',
            'image_path': ''
        }
    )
)


AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# If defined as a string new users will belong in this group. Group must exist
LDAP_AUTH_GROUP = None
# Whether new users will have admin access
LDAP_AUTH_IS_STAFF = False

# how many days should we keep data in the db
DATA_EXPIRES = '2'

LDAP_AUTH_SETTINGS = (
    { 'url': 'ldap://ds.example.org/', 'base': 'dc=noc,dc=example,dc=org' },
)
# If defined as a string new users will belong in this group. Group must exist
LDAP_AUTH_GROUP = None
# Whether new users will have admin access
LDAP_AUTH_IS_STAFF = False


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse'
#         }
#     },
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'filters': ['require_debug_false'],
#             'class': 'django.utils.log.AdminEmailHandler'
#         }
#     },
#     'loggers': {
#         'django.request': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#     }
# }
