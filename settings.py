# -*- coding:utf-8 -*-


# 基本配置
class Config():
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:rock1204" \
                              "@127.0.0.1:3306/coding_test"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "rock1204"


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    DEBUG = False
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
