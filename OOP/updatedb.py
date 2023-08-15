import shelve
db = shelve.open('persondb')
sue = db['Sue Petrov']
print(sue, sue.pay)
sue.give_raise(10)
db['Sue Petrov'] = sue
# for key in sorted(db):
#     print(key, '\t=>', db[key])
db.close()