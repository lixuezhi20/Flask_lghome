# @Time:     2022-05-09 : 15:20
from flask import Blueprint

api = Blueprint('api_1_0', __name__, url_prefix='/api/v1.0')


from . import dome
