import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    # ...
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:mysql123@localhost/t1'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


    # SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    
