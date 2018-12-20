# 引入Flask基本类库
from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import settings

from exts import db
from app.views import goodInfo

# 创建工程实例
app = Flask(__name__)
app.config.from_object(settings.DevelopmentConfig)
# 给数据库初始化app
db.init_app(app)

# 注册蓝图
app.register_blueprint(goodInfo)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

# 部署前 先删除migtations文件夹，在执行一下命令
# python manager.py db init
# python manager.py db migrate -m "create models"
# python manager.py db upgrade

if __name__ == "__main__":
    manager.run()
