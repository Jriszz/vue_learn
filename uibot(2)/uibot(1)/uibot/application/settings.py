# -*- coding: utf-8 -*-
"""Application configuration.

Most configuration is set via environment variables.

For local development, use a .env file to set
environment variables.
"""
#from environs import Env
import os
import timedelta
# env = Env()
# env.read_env()
# base_dir=os.path.abspath(os.path.dirname(__name__))
#ENV = env.str('FLASK_ENV', default='production')
# DEBUG = ENV == 'development'
path = os.path.abspath(os.path.dirname(__name__))

#database
USER = "test"
PASSWORD = "test"
DB_URL = "192.168.0.61:3306"
DATABASE_NAME = "testcasedata"
# USER = "root"
# PASSWORD = "zgf138138"
# DB_URL = "cdb-5vadfxqb.gz.tencentcdb.com:10065"
# DATABASE_NAME = "UiBot"
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{USER}:{PASSWORD}@{DB_URL}/{DATABASE_NAME}?charset=utf8"
SECRET_KEY = 'sercet_key'
CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_CHECK_DEFAULT=False
#session-setting
SESSION_PERMANENT=True
PERMANENT_SESSION_LIFETIME = timedelta.days=7
SESSION_TYPE='filesystem'
SESSION_FILE_DIR =  os.mkdir(os.path.join(path,'session'))if not os.path.exists(os.path.join(path,'session')) else os.path.join(path,'session')
SESSION_FILE_THRESHOLD = 1000
JSON_AS_ASCII = False
