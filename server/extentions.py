from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import CheckConstraint

db = SQLAlchemy()
migrate = Migrate()
