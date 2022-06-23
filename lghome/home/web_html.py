# @Time:     2022-05-09 : 16:34
# 提供静态文件
from flask import Blueprint, current_app, make_response
from flask_wtf import csrf

html = Blueprint('web_html', __name__)

# http://127.0.0.1:5000/static/html/index.html

# http://127.0.0.1:5000/
# http://127.0.0.1:5000/index.html
# http://127.0.0.1:5000/register.html


# 路由转换器
@html.route("/<re('.*'):html_file_name>")
def get_html(html_file_name):
    """提供HTML文件"""
    # print(html_file_name)
    # if html_file_name:
    #     html_file_name = 'html/' + html_file_name

    if not html_file_name:
        html_file_name = 'index.html'

    html_file_name = 'html/' + html_file_name

    # 生成CSRF的值
    csrf_token = csrf.generate_csrf()

    response = make_response(current_app.send_static_file(html_file_name))
    # 设置cookie
    response.set_cookie('csrf_token', csrf_token)

    # app.send_static_file()
    # flask提供的返回静态文件的方法
    return response
