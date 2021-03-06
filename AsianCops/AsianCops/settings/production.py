from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'wagtail',
        # 'USER': 'admin',
        # 'PASSWORD': DB_PW,
        # 'HOST': 'asian-cops-prod.cn0m6pjilrg2.us-east-1.rds.amazonaws.com',
        # 'PORT': 3306
        # figure out how to use the cnf file to hide username/password
        'OPTIONS': {
            # 'read_default_file': '/path/to/my.cnf',
            'init_command': "SET default_storage_engine=INNODB; \
             SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

DATABASES['default'].update(config['db_env'])
SECRET_KEY = config['secret_key']

STATIC_ROOT = config['static_root']
STATIC_URL = '/static/'

MEDIA_ROOT = config['media_root']
MEDIA_URL = '/media/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config['smtp_env']['host']
EMAIL_PORT = config['smtp_env']['port']
EMAIL_HOST_USER = config['smtp_env']['user']
EMAIL_HOST_PASSWORD = config['smtp_env']['password']
EMAIL_USE_TLS = eval(config['smtp_env']['use_tls'])
