from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# initialize the database
db = SQLAlchemy()
# initialize bcrypt
bcrypt = Bcrypt()