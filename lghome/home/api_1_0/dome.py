# @Time:     2022-05-09 : 15:27
from . import api
from home import db, models
import logging


@api.route('/index')
def index():
    logging.warning("测试")
    return "index_page"
