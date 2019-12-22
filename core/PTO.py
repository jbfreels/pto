import glob
import json
from os import path

class Year:
  total_pto = None
  dates = []
  def __init__ (self, json):
    self.json = json
    self.__dict__.update (self.json)

  def totalHours (self):
    return self.total_pto

  def totalRemaining (self):
    rem = self.total_pto
    for d in self.dates:
      rem -= self.dates[d]['hours']
    return rem

class PTO:
  def __init__ (self):
    self.years = self.load_json ()

  def load_json (self):
    years = []
    for j in glob.glob ("./json/*.json"):
      with open (j, 'r') as f:
        years.append (Year (json.loads (f.read ())))
    return years