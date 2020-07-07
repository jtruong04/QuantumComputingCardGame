import os
import urllib.parse
# from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG = False
    TESTING = False
    sql_user = 'root'
    sql_pwd = urllib.parse.quote_plus("QuantumCAT2020?")

    SQLALCHEMY_DATABASE_URI = ('mysql+pymysql://' + sql_user + ':'
                               + "QuantumCAT2020?"
                               + '@68.133.37.158/QuantumCat')
    SECRET_KEY = ('MICHAEL_SUCKS_AT_CODING_MAYBE')
    #SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')

class devConfig(Config):
    DEBUG = True
    TESTING = False

class prodConfig(Config):
#   overwrite to prod DB link
    pass