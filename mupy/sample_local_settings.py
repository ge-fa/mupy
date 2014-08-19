import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.join(BASE_DIR, 'mupy')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

SECRET_KEY = ''

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

MUNIN_NODES = (
    (
        1, {
            'name': 'main',
            'url': 'http://asd.example.org',
            'cgi_path': 'cgi-bin/munin-cgi-graph/',
            'image_path': ''
        }
    ),
)
MUNIN_URL = "http://munin.example.org"
#MUNIN_URL = "http://munin.ping.uio.no"
MUNIN_CGI_PATH = "cgi-bin/munin-cgi-graph/"
#MUNIN_CGI_PATH = ""
MUNIN_IMAGE_PATH = ""
#CACHE_BACKEND = 'dummy://'

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