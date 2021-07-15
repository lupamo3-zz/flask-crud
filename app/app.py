
from flask import Flask
from flask_migrate import Migrate

from .config import app_config
from .models import db, bcrypt

from .views.personalView import personal_api as personal_blueprint
from .views.certificateView import certificate_api as certificate_blueprint

def create_app(env_name):
  
  app = Flask(__name__)
#   app initialization

  app.config.from_object(app_config[env_name])
  """ 
  Initialize encryption and db connection
  """
  bcrypt.init_app(app)
  db.init_app(app)
  migrate = Migrate(app, db)

  app.register_blueprint(personal_blueprint, url_prefix='/api/v1/personal')
  app.register_blueprint(certificate_blueprint, url_prefix='/api/v1/certificate')
  @app.route('/', methods=['GET'])
  def index():
    """
    test  endpoint
    """
    return 'Congratulations!'

  return app