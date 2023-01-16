# 环境配置问题处理

1. 问题一：包的安装
- 问题：安装包时提示依赖pyproject.toml，但是pip安装pyproject.toml后，依然报错
- 处理：需要找到对应是那个包，然后下载对应的whl文件手动安装！
- 下载的文件还有一个问题就是，文件名和python版本是一一对应的，比如：backports.zoneinfo-0.2.1-cp38-cp381-win_amd64.whl，该文件对应的
是python3.8，但是当前python版本是3.11，只需要重命名文件名为：backports.zoneinfo-0.2.1-cp311-cp311-win_amd64.whl，再使用pip手动安装即可！

2. flask-migrate删除表
- 问题：配置flask-migrate后，执行flask db migrate -m 'remark'生成的python脚本每次都会删除数据库所有的表！
- 原因：flask-migrate版本升级后，改动比较大，剔除了MigrateCommand类，由此导致无法识别对应的表，导致每次都删除表
- 处理：实例化migrate的时候显式导入所有的模型即可
 ```
 from com.plugins import *
'''
flask-migrate4 issue解决：
此处需要显示导入所有的model，否则每次执行flask db migrate命令
生成的脚本会drop掉所有的表！
'''
from com.models import *

def reg_web_plugins(app):
    '''
    注册系统插件
    :param app:
    :return:
    '''
    db.init_app(app)
    bootstrap.init_app(app)
    # moment.init_app(app)
    mail.init_app(app)
    ckeditor.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    dropzone.init_app(app)
    login_manager.init_app(app)
    # babel.init_app(app)
    scheduler.init_app(app)
    scheduler.start()
 ```
