from classtools import AttrDisplay

class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    # def __repr__(self):   # used from AttrDisplay
    #     return f'{self.lastname()} is {self.job} earning {self.pay}'
    def lastname(self):
        return self.name.split()[-1]
    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent/100))

class Manager(Person):  # inheritance
    def __init__(self, name, pay):
        Person.__init__(self, name, 'Manager', pay)
    def give_raise(self, percent, bonus=10):
        Person.give_raise(self, percent+bonus)

# class Manager:    # delegation
#     def __init__(self, name, pay):
#         self.person = Person(name, 'Manager', pay)
#     def __getattr__(self, attr):
#         return getattr(self.person, attr)
#     def __repr__(self):
#         return str(self.person)
#     def give_raise(self, percent, bonus=10):
#         self.person.give_raise(percent + bonus)

class Department:   # composition
    def __init__(self, *args):
        self.members = list(args)
    def add_member(self, person):
        self.members.append(person)
    def give_raises(self, percent):
        for person in self.members:
            person.give_raise(percent)
    def show_all(self):
        for person in self.members:
            print(person)

if __name__ == '__main__':
    bob = Person('Bob Ivanov')
    sue = Person('Sue Petrov', job='Developer', pay=100000)
    print()
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print()
    print(sue.lastname())
    sue.give_raise(10)
    print(sue)
    print()
    tom = Manager('Tom Sidorov', 50000)
    tom.give_raise(10)
    print(tom.lastname())
    print(tom)
    print()
    development = Department(bob, sue)
    development.add_member(tom)
    development.give_raises(10)
    development.show_all()