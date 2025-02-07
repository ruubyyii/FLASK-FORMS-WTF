class Config():
    SECRET_KEY = 'ffcdda581e9cc9ecc582f0e894a325c1e90ac845c2b18b45e0daa6e6de742c97'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST= 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '1234567890'
    MYSQL_DB = 'flask_login'

class ProductionConfig(Config):
    DEBUG = True
    MYSQL_HOST= 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '1234567890'
    MYSQL_DB = 'flask_login'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
