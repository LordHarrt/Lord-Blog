from flask_script import Manager, Server
import main
import models


manager = Manager(main.app)

# Create a new commands: server
# This command will be run the Flask development_env server
manager.add_command("server", Server())


@manager.shell
def make_shell_context():
    """Create a python CLI"""
    # 确保有导入 Flask app object, 否则启动的CLI 上下文中仍然没有 app 对象
    return dict(app=main.app,
                db=models.db,
                User=models.User,
                Post=models.Post)

if __name__ == '__main__':
    manager.run()
