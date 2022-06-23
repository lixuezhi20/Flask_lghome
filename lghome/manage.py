# @Time:     2022-05-09 : 14:18
# 项目入口文件
from home import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from home import models

# 工厂模式
app = create_app('dev')

# 数据库迁移插件
manage = Manager(app)
Migrate(app, db)
manage.add_command("db", MigrateCommand)


if __name__ == '__main__':
    # app.run()
    manage.run()
