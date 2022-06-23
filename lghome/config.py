# @Time:     2022-05-09 : 14:41
import redis


class Config(object):
    """配置信息"""
    DEBUG = True

    # 数据库配置
    USERNAME = 'root'
    PASSWORD = '123456'
    HOSTNAME = '127.0.0.1'
    PORT = 3306
    DATABASE = 'lghome'

    # 数据库
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT,
                                                                             DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    REDIS_DB = 0

    # flask 需要加密
    SECRET_KEY = 'jdfsklaj#J$I#*%(U*DSJFLk'

    # flask-session
    SESSION_TYPE = "redis"  # 将session信息保存到redis中
    SESSION_REDIS = redis.Redis(host=REDIS_HOST,port=REDIS_PORT)
    SESSION_USE_SIGNER = True  # 对cookie中的session_id进行签名处理
    PERMANENT_SESSION_LIFETIME = 86400  # session数据的有效期


class DevConfig(Config):
    """开发环境的配置"""
    DEBUG = True


class ProConfig(Config):
    """生产环境配置"""
    DEBUG = False


config_map = {
    'dev': DevConfig,
    'pro': ProConfig
}