from app import db
from sqlalchemy.dialects.postgresql import JSON

class Users(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String())
  password = db.Column(db.String())
  username = db.Column(db.String())
  meta = db.Column(JSON)

  def __init__(self, email, password, username, meta):
    self.email = email
    self.username = username
    self.password = password
    self.meta = meta

  def __repr__(self):
    return '<id {}>'.format(self.id)
