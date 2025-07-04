import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'SECRET_KEY_NOT_SET')
    WTF_I18N_ENABLED = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True

    @classmethod
    def init_app(cls, app):
        print('!!!Run application in development mode.!!!')


class TestingConfig(Config):
    TESTING = True
    CSRF_ENABLED = False
    WTF_CSRF_ENABLED = False

    @classmethod
    def init_app(cls, app):
        print('!!!Run application in testing mode.!!!')


class ProductionConfig(Config):
    DEBUG = False
    USE_RELOADER = False

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)
        assert os.environ.get('SECRET_KEY'), 'SECRET_KEY IS NOT SET!'


config = {
    'default': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
