print(open(r'persondb.dir').read())
import shelve
db = shelve.open('persondb')
print(list(db.keys()))
bob = db['Bob Ivanov']
print(bob)
print(bob.lastname())