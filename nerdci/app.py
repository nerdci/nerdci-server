import falcon
import toml

from nerdci.db.manager import DBManager

class NerdCI(falcon.API):
  pass


with open("nerdci_server.toml") as cfg:
  config = toml.load(cfg)

dbmanager = DBManager(config["database"]["connection"])

api = falcon.API()
