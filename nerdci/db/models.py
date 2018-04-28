import sqlalchemy as sa

from sqlalchemy.ext.declarative import declarative_base


SAModel = declarative_base()


class Node(SAModel):
  __tablename__ = "nodes"
  id = sa.Column(sa.Integer, primary_key=True)
  address = sa.Column(sa.String(256), unique=True)
  friendly_name = sa.Column(sa.String(128), unique=True)

  def save(self, session):
    with session.begin():
      session.add(self)

