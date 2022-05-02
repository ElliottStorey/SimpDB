import json
import os

class SimpDB(object):
  def __init__(self, location: str):
    self.location = os.path.expanduser(location)
    if os.path.exists(self.location):
      self.db = json.load(open(self.location, "r"))
    else:
      self.db = {}

  def set(self, key: str, value: any):
    try:
      self.db[key] = value
      self.dump(self.db)
      return True
    except:
      return False

  def read(self, key: str):
    try:
      data = self.db[key]
      return data
    except:
      return False

  def delete(self, key: str):
    try:
      del self.db[key]
      self.dump(self.db)
      return True
    except:
      return False

  def load(self):
    try:
      return json.loads(self.db)
    except:
      return False

  def dump(self, data: json):
    try:
      json.dump(data, open(self.location, "w+"))
      return True
    except:
      return False
