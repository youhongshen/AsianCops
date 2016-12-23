from __future__ import absolute_import, unicode_literals

from .base import *
import json

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

with open(os.path.join(BASE_DIR, 'db-password.txt')) as f:
    DB_PW = f.read().strip()

with open(os.path.join(BASE_DIR, 'db_env.json')) as f:
    db_env = json.loads(f.read())

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'wagtail',
        # 'USER': 'admin',
        'PASSWORD': DB_PW,
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

DATABASES['default'].update(db_env)

with open(os.path.join(BASE_DIR, 'secret-key.txt')) as f:
    SECRET_KEY = f.read().strip()
