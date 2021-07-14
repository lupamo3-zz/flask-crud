from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt


# initialize the database
db = SQLAlchemy()
migrate = Migrate()
# initialize bcrypt
bcrypt = Bcrypt()