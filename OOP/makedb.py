from person import Person, Manager

bob = Person('Bob Ivanov')
sue = Person('Sue Petrov', job='developer', pay=100000)
tom = Manager('Tom Sidorov', 50000)

import shelve
db = shelve.open('persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()