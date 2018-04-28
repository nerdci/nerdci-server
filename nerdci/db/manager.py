import sqlalchemy
from sqlalchemy import orm
from sqlalchemy.orm import scoping

from nerdci.db import models


class DBManager(object):
  def __init__(self, connection=None):
    self.connection = connection

    self.engine = sqlalchemy.create_engine(self.connection)
    self.DBSession = scoping.scoped_session(
      orm.sessionmaker(
        bind=self.engine,
        autocommit=True
      )
    )

  @property
  def session(self):
    return self.DBSession()

  def setup(self):
    try:
      models.SAModel.metadata.create_all(self.engine)
    except Exception as e:
      print(f"Could not initialize DB: {e}")
