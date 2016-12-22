from __future__ import absolute_import, unicode_literals

from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

with open(os.path.join(BASE_DIR, 'db-password.txt')) as f:
    DB_PW = f.read().strip()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'wagtail',
        'NAME': os.getenv('DB_NAME'),
        # 'USER': 'admin',
        'USER': os.getenv('DB_USER'),
        'PASSWORD': DB_PW,
        # 'HOST': 'asian-cops-prod.cn0m6pjilrg2.us-east-1.rds.amazonaws.com',
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        # figure out how to use the cnf file to hide username/password
        'OPTIONS': {
            # 'read_default_file': '/path/to/my.cnf',
            'init_command': "SET default_storage_engine=INNODB; \
             SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

with open(os.path.join(BASE_DIR, 'secret-key.txt')) as f:
    SECRET_KEY = f.read().strip()
