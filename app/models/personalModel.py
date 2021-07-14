# src/models/UserModel.py
from marshmallow import fields, Schema
import datetime
from . import db

class personalModel(db.Model):
 
  __tablename__ = 'personal'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  email = db.Column(db.String(128), unique=True, nullable=False)
  password = db.Column(db.String(128), nullable=True)
  results = db.Column(db.String(128), nullable=False)
  course_name = db.Column(db.String(128), nullable=False)
  age = db.Column(db.Integer, nullable=False)
  student_applications = db.Column(db.Integer, nullable=False)
  created_at = db.Column(db.DateTime)
  modified_at = db.Column(db.DateTime)

 
  def __init__(self, data):
    """
    Class constructor
    """
    self.name = data.get('name')
    self.email = data.get('email')
    self.password = data.get('password')
    self.results = data.get("results")
    self.course_name = data.get("course_name")
    self.age = data.get("age")
    self.student_applications = data.get("student_applications")
    self.created_at = datetime.datetime.utcnow()
    self.modified_at = datetime.datetime.utcnow()

  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    for key, item in data.items():
      setattr(self, key, item)
    self.modified_at = datetime.datetime.utcnow()
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  @staticmethod
  def get_all_students():
    return personalModel.query.all()

  @staticmethod
  def get_one_student(id):
    return personalModel.query.get(id)

  
  def __repr(self):
    return '<id {}>'.format(self.id)