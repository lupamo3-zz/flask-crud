# src/models/certificateModel.py
from marshmallow import fields, Schema

from . import db
import datetime


class certificateModel(db.Model):
  """
  Certificate Model
  """

  __tablename__ = 'certificiatemodel'

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(128), nullable=False)
  contents = db.Column(db.Text, nullable=False)
  owner_id = db.Column(db.Integer, db.ForeignKey(
      'personal.id'), nullable=False)
  results = db.Column(db.String(128), nullable=False)
  course_name = db.Column(db.String(128), nullable=False)
  age = db.Column(db.Integer)
  student_applications = db.Column(db.Integer, nullable=True)
  created_at = db.Column(db.DateTime)
  modified_at = db.Column(db.DateTime)

  def __init__(self, data):
    self.title = data.get('title')
    self.contents = data.get('contents')
    self.results = data.get("results")
    self.course_name = data.get("course_name")
    self.age = data.get("age")
    self.student_applications = data.get("student_applications")
    self.owner_id = data.get('owner_id')
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
    de.session.commit()

  @staticmethod
  def get_all_certificates():
    return certificateModel.query.all()

  @staticmethod
  def get_one_certificate(id):
    return certificateModel.query.get(id)

  def __repr__(self):
    return '<id {}>'.format(self.id)


class certificateSchema(Schema):
  """
  certificateSchema Schema
  """
  id = fields.Int(dump_only=True)
  title = fields.Str(required=True)
  contents = fields.Str(required=True)
  results = fields.Str(required=True)
  course_name = fields.Str(required=True)
  age = fields.Int(required=True)
  student_applications = fields.Str(required=True)
  owner_id = fields.Int(required=True)
  created_at = fields.DateTime(dump_only=True)
  modified_at = fields.DateTime(dump_only=True)
