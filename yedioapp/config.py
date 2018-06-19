import os

class BaseConfig(object):
    pass


class DevelopementConfig(BaseConfig):
    pass

class ProductionConfig(BaseConfig):
    DEBUG = False


config = {
    'development': DevelopementConfig,
    'production': ProductionConfig
}