''' setting api config '''


''' base  config class '''
class Config(object):
    DEBUG=False
    SECRET_KEY="secret"

''' testing class configurations '''
class Testing(Config):
    DEBUG=True
    TESTING=True

''' dev class configurations '''
class Development(Config):
    DEBUG=True

''' staging configurations '''
class Staging(Config):
    DEBUG=False
    
''' production configurations '''
class Production(Config):
    DEBUG=False
    TESTING=False



api_config={
'development':Development,
'testing':Testing,
'staging':Staging,
'production':Production,
}