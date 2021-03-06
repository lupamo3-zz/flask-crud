# src/models/UserModel.py
from marshmallow import fields, Schema
import datetime

from . import db
from .certificateModel import certificateModel, certificateSchema
from ..app import bcrypt


class personalModel(db.Model):

  __tablename__ = 'personal'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  email = db.Column(db.String(128), unique=True, nullable=False)
  password = db.Column(db.String(128), nullable=True)
  created_at = db.Column(db.DateTime)
  modified_at = db.Column(db.DateTime)
  certificates = db.relationship(
      'certificateModel', backref='personal', lazy=True)


  def __init__(self, data):
    """
    Class constructor
    """
    self.name = data.get('name')
    self.email = data.get('email')
    self.password = self.__generate_hash(data.get('password'))
    self.created_at = datetime.datetime.utcnow()
    self.modified_at = datetime.datetime.utcnow()

  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    for key, item in data.items():
        if key == 'password':  # add this new line
            self.password = self.__generate_hash(value)
        setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def __generate_hash(self, password):
    return bcrypt.generate_password_hash(password, rounds=10).decode("utf-8")

  def check_hash(self, password):
    return bcrypt.check_password_hash(self.password, password)

  @staticmethod
  def get_all_students():
    return personalModel.query.all()

  @staticmethod
  def get_one_student(id):
    return personalModel.query.get(id)

  @staticmethod
  def get_user_by_email(value):
      return personalModel.query.filter_by(email=value).first()

  
  def __repr(self):
    return '<id {}>'.format(self.id)


class personalSchema(Schema):
    """
    personal Schema
    """
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
    certificates = fields.Nested(certificateSchema, many=True)
