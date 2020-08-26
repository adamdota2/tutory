import os
import config
from flask import Flask
from models.base_model import db
from models.user import User
from flask_jwt_extended import JWTManager
  
web_dir = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'tutory_web')

app = Flask('TUTORY', root_path=web_dir)
jwt = JWTManager(app)

if os.getenv('FLASK_ENV') == 'production':
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

# login_manager = LoginManager()
# login_manager.init_app(app) # configure the app for flask-login

# login_manager.login_view = "home"   # if user try to access login_required route without sign in, will redirect to `home`
# login_manager.login_message = "Please log in before proceeding"
# login_manager.login_message_category = "warning"

# # This callback is used to reload the user object from the user ID stored in the session.
# @login_manager.user_loader
# def load_user(user_id):
#     return User.get_or_none(User.id == user_id)

# @app.before_request
# def before_request():
#     db.connect()

@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        print(db)
        print(db.close())
    return exc
