# @Time:     2022-05-09 : 14:53
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
import redis
from config import config_map
import logging
from logging.handlers import RotatingFileHandler
from home.utils.commons import ReConverter

# 数据库
db = SQLAlchemy()

# 创建Redis连接对象
redis_store = None


def setup_log():
    # error 错误级别
    # warning 警告级别
    # info 信息提示
    # debug 调试级别
    # 设置日志的的等级  DEBUG调试级别
    logging.basicConfig(level=logging.DEBUG)
    # 创建日志记录器，设置日志的保存路径和每个日志的大小和日志的总大小
    # 如果文件超过100M 就新建一个文件log.log log1.log
    file_log_handler = RotatingFileHandler("logs/log.log", maxBytes=1024 * 1024 * 100, backupCount=100)
    # 创建日志记录格式，日志等级，输出日志的文件名 行数 日志信息
    formatter = logging.Formatter("%(levelname)s %(filename)s: %(lineno)d %(message)s")
    # 为日志记录器设置记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flaks app使用的）加载日志记录器
    logging.getLogger().addHandler(file_log_handler)


# 工厂模式 config_name => dev 开发模式去创建app  config_name => pro 用生产模式去创建app
def create_app(config_name):
    """
    创建flask的应用对象
    :param config_name:str 配置模式的名字
    :return:app
    """
    setup_log()
    app = Flask(__name__)

    # if config_name == 'dev':
    #     from config import DevConfig
    #     app.config.from_object(DevConfig)
    # else:
    #     from config import ProConfig
    #     app.config.from_object(ProConfig)

    config_class = config_map.get(config_name)
    app.config.from_object(config_class)

    # 初始化db
    db.init_app(app)

    global redis_store
    redis_store = redis.Redis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT)

    # session和cookie session信息就会被保存到redis中
    Session(app)

    # 为flask添加防护机制
    CSRFProtect(app)

    # 为flask添加自定义的转换器
    app.url_map.converters['re'] = ReConverter

    # 注册蓝图
    from home import api_1_0
    app.register_blueprint(api_1_0.api)

    # 注册提供静态文件的蓝图
    from home import web_html
    app.register_blueprint(web_html.html)

    return app