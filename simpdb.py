import json
import os

class SimpDB(object):
  def __init__(self, location: str):
    self.location = os.path.expanduser(location)
    if os.path.exists(self.location):
      self.db = json.load(open(self.location, "r"))
    else:
      self.db = {"meta": {"id": 0}}

  def create(self, data):
    try:
      id = self.db["meta"]["id"] + 1
      self.db["meta"]["id"] += 1
      self.db[id] = data
      self.dump(self.db)
      return id
    except:
      return False

  def read(self, id):
    try:
      data = self.db[id]
      return data
    except:
      return False
  
  def update(self, id: str, key: str, value):
    try:
      self.db[id][key] = value
      self.dump(self.db)
      return True
    except:
      return False

  def delete(self, id):
    try:
      del self.db[id]
      return True
    except:
      return False

  def load(self):
    try:
      return json.loads(self.db)
    except:
      return False

  def dump(self, data):
    try:
      json.dump(data, open(self.location, "w+"))
      return True
    except:
      return False
