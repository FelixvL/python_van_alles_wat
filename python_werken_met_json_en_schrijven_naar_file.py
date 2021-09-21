import json
from types import SimpleNamespace

data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'

# Parse JSON into an object with attributes corresponding to dict keys.
x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
print(x.name, x.hometown.name, x.hometown.id)

print("=========================")

mijna = ["hoi","daar"]
f = open("demofile2.txt", "a")  # w mag ook
stukstring = " "

f.write("Now the file has more content!")
f.close()

print("=========================")

import json
from collections import namedtuple

data = '{"name": "John Smith", "hometown": {"name": "New York", "id": 123}}'

# Parse JSON into an object with attributes corresponding to dict keys.
x = json.loads(data, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
print(x)
print(x.name)

print("=========================")

class Drank:
    prijs = 25
    naam = "test"
    def drnaarcsv(self):
        return str(self.prijs)+","+self.naam

d1 = Drank()    
print(d1.drnaarcsv())    
mijna = [Drank(),Drank(),Drank()]
mijnb = []
for dr in mijna:
    mijnb.append(dr.drnaarcsv())

f = open("demofile2.txt", "w")
stukstring = ";"
#stukstring = stukstring.join(mijna) # werkt niet
stukstring = stukstring.join(mijnb)

f.write(stukstring)
f.close()
stukstring