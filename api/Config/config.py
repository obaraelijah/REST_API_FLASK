import os
from decouple import config


class Config:
    SECRET_KEY=config('SECRET_KEY','Secret')
    
    
class DevConfig(Config):
    DEBUG=config('DEBUG',cast=bool)
    
    
class Testconfig(Config):
    pass


class ProdConfig(Config):
    pass
    
    

config_dict={
    'dev':DevConfig,
    'prod':ProdConfig,
    'test':Testconfig
}