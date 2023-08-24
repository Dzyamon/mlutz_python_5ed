# ---RUN A PYTHON---

# import module1
# from module1 import b,c
# reload(module1.py)
# exec(open('module1.py').read())
# # FOR UNIX:
# chmod +x file.py
# file.py:
# #!usr/bin/env python3
# print('Test')

# ---TYPES AND OPERATIONS---

# import math
# math.floor(2.5) -> 5 // 2 -> 2
# math.floor(-2.5) -> 5 // -2 -> -3
# math.trunc(2.5) -> int(-2) -> 2
# math.trunc(-2.5) -> int(-2.5) -> -2
# hex(64) -> 0x40 
# 64 -> int('40', 16) -> int('0x40', 16) -> eval('0x40')
# bin(0b0001<<3) -> '0b1000' # BITWISE SHIFT LEFT
# bin(0b0001 | 0b010) -> '0b11' # BITWISE OR
# bin(0b0001 & 0b10) -> '0b0' # BITWISE AND
# bin(0b0001 ^ 0b101) -> '0b100' # BITWISE XOR
# 0b1100011.bit_length() -> 7

# import random
# random.choice(['a', 'b', 'c'])
# lst = ['a', 'b', 'c']
# random.shuffle(lst)

# import decimal
# decimal.Decimal('0.1') + decimal.Decimal('0.10') -> Decimal('0.20')
# decimal.getcontext().prec = 4
# # temp precision
# with decimal.localcontext() as ctx:
#     ctx.prec = 2
#     decimal.Decimal('1.00') / decimal.Decimal('3.00') -> Decimal('0.33')

# import fractions
# fractions.Fraction('.25') -> Fraction(1, 4)
# fractions.Fraction(*(2.5).as_integer_ratio()) -> Fraction(5, 2)
# fractions.Fraction.from_float(1.75) -> Fraction(7, 4)

# S=set(1.23)
# S.add((1, 2, 3)) # only tuples could be added

# #garbage collector
# import sys
# x=[]
# print(sys.getrefcount(x)) -> 2
# def bar(a):
#     print(sys.getrefcount(a))
# bar(x) -> 4
# print(sys.getrefcount(x)) -> 2

# import copy
# A,B,C=[],set(),{}
# Y = copy.copy(A)
# Y = copy.copy(B) # Make top-level "shallow" copy of any object Y
# Y = copy.deepcopy(C) # Make deep copy of any object Y: copy all nested parts

# == - True if two referenced objects have the same values
# is - True if both names point to the exact same object
# !small ints are not garbage collected

# reply = """
# Greetings...
# Hello %(name)s!
# Your age is %(age)s
# """
# values = {'name': 'Bob', 'age': 40} 
# print(reply % values)
# food = 'spam'
# print('more %(food)s' % vars())
# import sys
# 'My {map[kind]} runs {sys.platform}'.format(sys=sys, map={'kind': 'laptop'})
# -> 'My laptop runs win32'
# print('{0:>10} = {1:>010.2f}'.format('spam', 123.4567))
# -> '      spam = 0000123.46'

# L = [1, 2, 3]
# L[1:2] = [4, 5]
# -> [1, 4, 5, 3] # replace with several
# L = [1]
# L[:0] = [2, 3, 4] 
# -> [2, 3, 4, 1] # insert unpacked at the beginning
# L.insert(0, [2, 3, 4]) 
# -> [[2, 3, 4], 1] # insert packed
# l.append(x) === l+=[x] # same object _is_ True
# l+=[x] != l=l+[x] # new object
# L = ['abc', 'ABD', 'aBe']
# L.sort(key=str.lower, reverse=True)
# -> ['aBe', 'ABD', 'abc']
# .sort(), .reverse() # change object and returns None
# sorted(), reversed() # don't change object and returns new list/reversediterator
# .append() # adds one
# .extend() # adds many items
# .remove() # delete by value L.remove('eggs')
# .pop() # delete by index and returns deleted
# del l[-1] or del l[1:] == l[1:]=[] # delete by index or slice

# d.get(key, default) # dict doesnt changed if new key
# d.setdefault(key, default) # new key is added to the dict
# d.items() -> (key, value)
# d.fromkeys(['a', 'b'], 0) == {k:0 for k in 'ab'} -> {'a': 0, 'b': 0}
# dict(sorted(d.items())) # sort by key
# dict(sorted(d.items(), key=lambda item: item[1])) # sort by value

# import pickle
# D = {'a': 1, 'b': 2}
# F = open('datafile.pkl', 'wb')
# pickle.dump(D, F)
# F.close()
# F = open('datafile.pkl', 'rb')
# E = pickle.load(F)

# import json
# rec = {'job': ['dev', 'mgr'], 'name': {'last': 'Smith', 'first': 'Bob'}, 'age': 40.5}
# json.dump(rec, fp=open('testjson.txt', 'w'), indent=4)
# print(open('testjson.txt').read())
# print(json.load(open('testjson.txt')))

# import struct
# F = open('data.bin', 'wb')
# data = struct.pack('>i4sh', 7, b'spam', 8)
# F.write(data)
# F.close()
# F = open('data.bin', 'rb')
# data = F.read()
# values = struct.unpack('>i4sh', data) -> (7, b'spam', 8)

# with open('myfile.txt', 'w') as f:
#     f.write("Hello file world!")
# print(open("myfile.txt").read())

#----- STATEMENTS AND SYNTAX ------

# ((a, b), c) = ('SP', 'AM')
# -> a, b, c === ('S', 'P', 'AM')
# unpacking with * always returns a list
# a, *b, c = 'spam'
# a, b, c == ('s', ['p', 'a'], 'm')
# for mutables L = L + .. creates new objects, but L+= ... changes L in place   
# A = ((X and Y) or Z) === A = Y if X else Z === A = [Z, Y][bool(X)]
# dict(zip(keys, vals)) === {k: v for (k, v) in zip(keys, vals)}
# import os
# for line in os.popen('systeminfo'): 
#     print(line.rstrip().encode('cp1251').decode('cp866'))

# I=iter(range(5))
# E=iter(enumerate(str))
# next(I) 
# next(E)
# L=iter(list) -> L.__next__() === next(L)
# next(file) and next(map, zip, filter) -> no need for iter()
# range, dict+dict.keys.values.items() -> needs iter()
# Every generator is an iterator, but not vice versa. 
# iterator has __iter__ and __next__
# generator use yield or () comprehension
# enumerate(), iter(), reversed(), and MZF(map,zip,filter)  - are generators that return iterators

# python -m pydoc -b # docstring help()

# --EXCERCISE--

# s='abcde'
# print(sum([ord(c) for c in s]))
# print(list(map(ord,s)))
# d={'a':1, 'c':3, 'b':2}
# for k,v in sorted(d.items()):
#     print(k,v)
# L = [2**X for X in range(7)]
# L = list(map(lambda x: 2 ** x, range(7)))
# X = 5
# if 2**X in L:
#     print('at index', L.index(2**X))
# else:
#     print(X, 'not found')

# ---------FUNCTIONS AND GENERATORS-------

# in def could use global but to change it should be declared global
# LOCAL -> NONLOCAL -> GLOBAL -> BUILTINS (search in that order)
# def maker(N):
#     return lambda X: X**N
# h = maker(3)
# h(4) ==> 64
# def makeActions():
#     acts = []
#     for i in range(3): # Use defaults instead
#         acts.append(lambda x, i=i: i ** x) # i=i - remembers current i
#     return acts
# acts = makeActions()
# print(acts[0](2))
# Nonlocals must already exist in enclosing def!
# Globals don't have to exist yet when declared - they are created
# Using nonlocal - variable must be in a def, not in the module
# def tester(start):
#     state = start
#     def nested(label):
#         nonlocal state
#         print(label, state)   
#         state += 1     
        # print(label, nested.state)     # state with function attribute
        # nested.state += 1              # without nonlocal
    # nested.state = start               # after nested def
#     return nested
# F=tester(1)
# G=tester(11)
# F('a') -> a 1
# F('b') -> b 2
# G('b') -> b 11
# F('c') -> c 3
# G('c') -> c 12
# functions might update mutable objects like lists and dictionaries passed into them
# X=1; L=[1,2]
# X,L = multiple(X,L) == return new X,L -> change X L
# def f(a, *pargs, **kargs): print(a, pargs, kargs)
# f(1, 2, 3, x=1, y=2)
# -> 1 (2, 3) {'y': 2, 'x': 1}
# func(1, c=3, *(2,), **{'d': 4}) # Same as func(1, 2, c=3, d=4)
# -> 1 2 3 4
# def func(a,*,b,c): -> * means that no var-length parameters and b,c are keywords-only
# def func(a, /, b="~", *, c=50): positional-only, regular, and keyword-only arguments separated by / and *
# def func(a,*,b='default1',c='default2'): -> func(1) only a is required by position or by name
# def func(a,*,b=1,c,d=2): -> func(3, c=4, b=5) c= is required
# def func(a, **, b, c): -> error
# func((a, *b, c=6, **d) -> collect in dictionary func(1,2,c=4,d=5) -> 1 (2,) 6 {'a':4, 'b':5}
# func(1, *(2, 3), **dict(x=4, y=5)) -> unpacking values (the same result): 1 (2, 3) 6 {'y': 5, 'x': 4}
# func(1, *(2, 3), **dict(x=4, y=5), c=7) -> invalid
# func(1, *(2, 3), **dict(x=4, y=5, c=7)) -> ok
# def func(a, b, c): 
#     a = 2
#     b[0] = 'x'
#     c['a'] = 'y'
# l=1; m=[1]; n={'a':0}
# func(l, m, n)
# print(l,m,n) # only list change as mutable object

# RECURSION
# def sumtree(L):
#     tot = 0
#     for x in L: # For each item at this level
#         if not isinstance(x, list):
#             tot += x # Add numbers directly
#         else:
#             tot += sumtree(x) # Recur for sublists
#     return tot
# def sumtree2(L): # queue/stack examples
#     tot = 0
#     items = list(L) # Start with copy of top level
#     while items:
#         front = items.pop(0) # Fetch/delete front item
#         if not isinstance(front, list):
#             tot += front # Add numbers directly
#         else:
#             items.extend(front) # <== Append all in nested list === FIFO
#             #items[:0] = front # <== Prepend all in nested list === LIFO
#     return tot
# L = [1, [2, [3, 4], 5], 6, [7, 8]] # Arbitrary nesting
# print(sumtree2(L))
# lambda x, y: x + y === operator.add

# tkinter Button example
# import sys
# from tkinter import Button, mainloop
# x = Button(text='Press me', command=(lambda:sys.stdout.write('Spam\n'))) 
# x.pack()
# mainloop()

# !generators use iter protocol!
# generator YIELD: generates one at a time, suspending and resuming their state and retain their local vars
# def gen(n):
#     for i in range(n):
#         X = yield i
#         print(X)
# G = gen(3)
# print(next(G)) #-> 0
# print(G.send(88)) #-> 88 1 # generator returns the value passed to send
# print(next(G)) #-> None 2
# generator expression - return an object that produces results on demand instead of complete list
# G = (x ** 2 for x in range(4))
# next(G) -> no need iter()
# Generators - is one-pass iterator and is exhausted after one pass
# for i in range(N): yield i === yield from range(N)

# import os
# for (root, subs, files) in os.walk('.'): # Directory walk generator
#     print(root, subs, files)

# def permute1(seq):
#     if not seq: # Shuffle any sequence: list
#         return [seq] # Empty sequence
#     else:
#         res = []
#         for i in range(len(seq)):
#             rest = seq[:i] + seq[i+1:] # Delete current node
#             for x in permute1(rest): # Permute the others
#                 res.append(seq[i:i+1] + x) # Add node at front
#         return res
# print(permute1([1,2,3]))
# def permute2(seq):
#     if not seq: # Shuffle any sequence: generator
#         yield seq # Empty sequence
#     else:
#         for i in range(len(seq)):
#             rest = seq[:i] + seq[i+1:] # Delete current node
#             for x in permute2(rest): # Permute the others
#                 yield seq[i:i+1] + x # Add node at front
# print(list(permute2([1,2,3])))

# def recursive_factorial(n):
#     if n == 1: return n
#     else: return n*recursive_factorial(n-1)
# print(recursive_factorial(5))
# def yield_factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#         yield result
# x=1
# for i in yield_factorial(5):
#     print(f'Factorial for {x} -> {i}')
#     x+=1

# set comprehension: {x * x for x in range(10)} === set(x * x for x in range(10))
# dict comprehension: {x: x * x for x in range(10)} === dict((x, x * x) for x in range(10))

# --EXCERCISE--
# RUN IN COMMAND PROMT: >python study_book.py

# def adder1(*args):
#     sum = args[0] 
#     for i in args[1:]:
#         sum += i 
#     return sum
# print(adder1(1,2,3)) --> 6
# print(adder1('a','b')) --> ab
# print(adder1(['a', 1], {'c', 3})) --> ['a', 1, 'c', 3]

# def adder2(a=1, b=2, c=3):
#     return a+b+c
# print(adder2(4, c=6)) --> 12

# def adder3(**kwargs):
#     sum=0
#     for v in kwargs.values():
#         sum += v 
#     return sum
# print(adder3(a=1, c=6, b=7)) --> 14
# #v2
# def adder3(**args):
#     return adder1(*args.values())
# print(adder4(a=1, c=6, b=7)) --> 14

# def copyDict(old): # d2=d1.copy() 
#     new={}
#     for k in old.keys():
#         new[k]=old[k]
#     return new
# d1={'a': 1, 'b': 2}
# d2=copyDict(d1)
# d1['b']=3
# print(d1, d2)

# def addDict(d1,d2): # and d1.update(d2) - returns None, but changes d1
#     new={}
#     for k in d1.keys():
#         new[k]=d1[k]
#     for k in d2.keys():
#         new[k]=d2[k]
#     return new
# d1={'a': 1, 'b': 2}
# d2={'c': 3, 'b': 4}
# d3=addDict(d1,d2)
# print(d3) --> {'a': 1, 'b': 4, 'c': 3}

# def f1(a, b): print(a, b) # Normal args
# f1(1, 2) === f1(b=2, a=1) --> 1 2
# def f2(a, *b): print(a, b) # Positional varargs
# f2(1, 2, 3) --> 1 (2,3)
# def f3(a, **b): print(a, b) # Keyword varargs
# f3(1, x=2, y=3) --> 1 {'x':2, 'y':3}
# def f4(a, *b, **c): print(a, b, c) # Mixed modes
# f4(1, 2, 3, x=2, y=3) --> 1 (2,3) {'x':2, 'y':3}    
# def f5(a, b=2, c=3): print(a, b, c) # Defaults
# f5(1) --> 1 2 3
# f5(1, 4) --> 1 4 3
# def f6(a, b=2, *c): print(a, b, c) # Defaults and positional varargs
# f6(1) --> 1 2 ()
# f6(1, 3, 4) --> 1 3 (4,)

# def prime(y):
#     if y <= 1:
#         print(y, 'not prime')
#     else:
#         x = y // 2
#         while x > 1:
#             if y % x == 0: # Remainder
#                 print(y, 'has factor', x)
#                 break
#             x -= 1
#         else:
#             print(y, 'is prime')
# prime(34)

# import math
# L=[2, 4, 9, 16, 25]
# SL1=[math.sqrt(i) for i in L] # list comprehension
# SL2=list(map(math.sqrt, L))  # map
# SL3=list(math.sqrt(i) for i in L)  # generator
# print(SL1,SL2,SL3)

# BENCHMARKING & TIMEIT module

# from timeit import repeat
# from math import sqrt
# def fn1(n):
#     return sqrt(n)
# def fn2(n):
#     return n**0.5
# def fn3(n):
#     return pow(n, 0.5)
# for test in (fn1, fn2, fn3):
#     print(test.__name__.rjust(10, ' '), '\t', min(repeat(stmt=lambda: test(500), number=20, repeat=3)))

# import timeit
# # binary search function
# def binary_search(mylist, find):
# 	while len(mylist) > 0:
# 		mid = (len(mylist))//2
# 		if mylist[mid] == find:
# 			return True
# 		elif mylist[mid] < find:
# 			mylist = mylist[:mid]
# 		else:
# 			mylist = mylist[mid + 1:]
# 	return False
# # linear search function
# def linear_search(mylist, find):
# 	for x in mylist:
# 		if x == find:
# 			return True
# 	return False
# # compute binary search time
# def binary_time():
# 	SETUP_CODE = '''
# from __main__ import binary_search
# from random import randint
#     '''
# 	TEST_CODE = '''
# mylist = [x for x in range(10000)]
# find = randint(0, len(mylist))
# binary_search(mylist, find)
#     '''
# 	times = timeit.repeat(setup=SETUP_CODE,
# 						stmt=TEST_CODE,
# 						repeat=3,
# 						number=10000)
# 	print(f'Binary search time: {min(times)}')
# # compute linear search time
# def linear_time():
# 	SETUP_CODE = '''
# from __main__ import linear_search
# from random import randint
#     '''
# 	TEST_CODE = '''
# mylist = [x for x in range(10000)]
# find = randint(0, len(mylist))
# linear_search(mylist, find)
# 	'''
# 	times = timeit.repeat(setup=SETUP_CODE,
# 		                stmt=TEST_CODE,
# 						repeat=3,
# 						number=10000)
# 	print(f'Linear search time: {min(times)}')
# if __name__ == "__main__":
#     binary_time()
#     linear_time()

# def countdown(x):
#     try:
#         while x>0:
#             print(x, end=' ')
#             x-=1
#     finally:
#         print('stop')
# #v2
# def countdown(n):
#     if n==0:
#         print('stop') 
#     else:
#         print(n, end=' ')
#         countdown(n-1)
# countdown(5)
# def countdown2(n): # Generator function, recursive
#     if n == 0:
#         yield 'stop'
#     else:
#         yield n
#         for x in countdown2(n-1):
#             yield x 
#         # yield from countdown2(n-1)
# G=countdown2(5)
# for i in range(6):
#     print(next(G))

# from timeit import repeat
# from functools import reduce
# from math import factorial
# def recursive_factorial(n):
#     if n == 1: return n
#     else: return n*recursive_factorial(n-1)
# def iterative_factorial(n):
#     res = 1
#     for i in range(1, n+1): 
#         res *= i
#     return res
# def reduce_factorial(n):
#     return reduce(lambda a, b: a*b, range(1,n+1))
# def math_factorial(n):
#     return factorial(n)
# for test in (recursive_factorial, reduce_factorial, iterative_factorial, math_factorial):
#     print(test.__name__.rjust(20, ' '), '\t', min(repeat(stmt=lambda: test(500), number=20, repeat=3)))

# --------MODULES AND PACKAGES-----------

# import module1
# print(dir(module1))
# print(module1.__file__)
# print(module1.__dict__.keys())
# print(list(name for name in module1.__dict__))
# mod1->mod2->mod3
# mod1:
# import mod2 - files import
# import mod2.mod3 - package (directory trees) imports 
# print(mod2.mod3.X) --> nested import

# from importlib import reload
# reload(module1)
# module1.func()

# from string import name # imports string from sys.path
# from .pkg import string # import string from current package . /relative
# from mypkg import string # /absolute
# >>> import pkg.main
# __init__.py present
# pkg/main.py
# pkg/string.py and ./string
# from . import string -> reads file inside package pkg
# import string -> reads file outside package in cwd, but not in sys.path lib
# print(string)

# import and from ... import ... - both import entire module, but from copies vars in namespace
# module is imported only once per process
# package (with relative imports = from . import mod) >>> import pkg.mod
# executable program (with simple imports = import mod) >>> python pkg\mod.py
# both (from system.section.mypkg import mod)

# https://www.tutorialspoint.com/How-to-set-python-environment-variable-PYTHONPATH-on-Linux
# # check current environments sys.path
# python -c "import sys; print('\n'.join(sys.path))"
# [linux] echo $PYTHONPATH
# [linux] export PYTHONPATH=.:$PYTHONPATH  # add current cwd to pythonpath
# # same result as package and executable script:
# python pkg\main.py
# >>> import pkg.a

# 2 models: regular and namespace package (only dir - without __init__.py)
# in Windows PS-> rundll32 sysdm.cpl,EditEnvironmentVariables
# regular package priority over same-named namespace package

# from unders import * # Load non _x names only
# import mod
# mod._x -> successfully import _x
# _all__ identifies names to be copied
#
# # runme.py
# def tester():
#     print("Test...")
#     print(__name__)
# if __name__ == '__main__':
#     tester()
# > python runme.py
# >>> import runme
# >>> runme.tester()

# sys.path.append('C:\\sourcedir')
# sys.path - only running program, PYTHONPATH - permantent

# >>> modname = 'string'
# >>> exec('import ' + modname)
# >>> string
#v2
# >>> import importlib
# >>> modname = 'string'
# >>> string = importlib.import_module(modname)
# >>> string

# to change X use:
# import mod1 mod1.X=111 vs [NOT] from mod1 import X, X=111
# to reload use:
# import module vs [NOT] from module import X
# reload(module)
# module.X
# to reload fuction after change:
# from imp import reload
# import module
# reload(module)
# from module import function
# function(1, 2, 3)

#-------CLASSES AND OOP-----------

# class C2: pass
# class C3: pass
# class C1(C2, C3):
#     def __init__(self, who):
#         self.name = who
# I1 = C1('bob')
# print(I1.name)

# class FirstClass:
#     def setdata(self, value):
#         self.data = value
#     def display(self):
#         print(self.data)
# x = FirstClass()
# x.setdata('KKK')
# x.display()
# x.data='NEW'
# x.display()

# # from modulename import FirstClass
# # or import modulename -> class SecondClass(modulename.FirstClass)
# class SecondClass(FirstClass):
#     def display(self):
#         print(f'Current value = {self.data}')
# y = SecondClass()
# y.setdata(42)
# y.display()

# class ThirdClass(SecondClass):
#     def __init__(self, value):
#         self.data = value
#     def __add__(self, other):
#         return ThirdClass(self.data + other)
#     def __str__(self):
#         return f'ThirdClass: {self.data}'
#     def mul(self, other):
#         self.data *= other
# a = ThirdClass('abc')
# a.display()
# print(a)
# b=a+'xyx'
# print(b.data)
# b.display()
# a.mul(3)
# print(a)

# class rec:
#     pass
# rec.name='Adnan'
# x=rec()
# print(x.name)
# x.name='Maksim'
# print(rec.name, x.name)
# print(rec.__dict__, x.__dict__)

# print(open(r'OOP\persondb.dir').read())
# import shelve, sys, os
# sys.path.append(os.path.join(os.path.dirname(__file__), 'OOP'))
# #print(sys.path)
# # #v2
# # from pathlib import Path
# # shelfSavePath = Path(sys.argv[0]).parent / Path('OOP\persondb')
# # db = shelve.open(fr'{shelfSavePath}')
# db = shelve.open('OOP\persondb')
# print(list(db.keys()))
# bob = db['Bob Ivanov']
# print(bob)
# print(bob.lastname())

# class MixedNames:
#     data = 'spam'
#     def __init__(self, value):
#         self.data = value
#     def display(self):
#         print(self.data, MixedNames.data)
# x = MixedNames(1)
# y = MixedNames(2)
# print(x.display(), y.display())

# class NextClass:
#     def printer(self, text):
#         self.message = text
#         print(self.message)
# x = NextClass()
# x.printer('instance call')  # better
# print(x.message)
# NextClass.printer(x, 'class call')
# print(x.message)

# class Super:
#     def method(self):
#         print('in Super.method')
#     def delegate(self):
#         self.action()
# class Inheritor(Super):
#     pass
# class Replacer(Super):
#     def method(self):
#         print('in Replacer.method')
# class Extender(Super):
#     def method(self):
#         print('starting Extender.method')
#         Super.method(self)
#         print('ending Extender.method')
# class Provider(Super):
#     def action(self):
#         print('in Provider.action')
# if __name__ == '__main__':
#     for klass in (Inheritor, Replacer, Extender):
#         print('\n' + klass.__name__ + '...')
#         klass().method()
#     print('\nProvider...')
#     x = Provider()
#     x.delegate()

# #import manynames.py
# X = 11
# def f():
#     print(X)
# def g():
#     X = 22
#     print(X)
# def g2():
#     global X
#     X = 22
# def h1():
#     X = 33
#     def nested():
#         print(X)
#     nested()
# def h2():
#     X = 33
#     def nested():
#         nonlocal X
#         X = 44
#     nested()
#     print(X)
# class C:
#     X = 33
#     def m(self):
#         X = 44
#         self.X = 55
# if __name__ == '__main__':
#     print(X) # 11
#     f() # 11
#     g() # 22
#     g2() # g2() changed global X to 22
#     print(X) # 22
#     h1() # 33
#     h2() # 44
#     #print(X) # 33
#     obj = C()
#     print(obj.X, C.X) # 33 33
#     obj.m()
#     print(obj.X) # 55
#     print(C.X) # 33
#     #print(C.m.X) # FAILS: only visible in method
#     #print(g.X) # FAILS: only visible in function
# import manynames
# print(manynames.X) # 11
# manynames.f() # 11
# manynames.g() # 22
# print(manynames.C.X) # 33
# I = manynames.C()
# print(I.X) # 33
# I.m()
# print(I.X) # 55

# X = 1
# def nester():
#     X = 2 # replace global X=1
#     print(X) # 2
#     class C:
#         X = 3
#         print(X) # 3
#         def method1(self):
#             print(X) # 2 - use X from nested
#             print(self.X) # 3 - use X from class
#         def method2(self):
#             X = 4
#             print(X) # 4
#             print(self.X)  # 3
#             self.X = 5
#             print(self.X) # 5
#     I = C()
#     I.method1()
#     I.method2()
# print(X) # 1
# nester()
# print('-'*40)

# class Super:
#     def hello(self):
#         self.data1 = 'hi'
# class Sub(Super):
#     def hola(self):
#         self.data2 = 'priv'
# x = Sub()
# print(x.__dict__)
# print(x.__class__)
# print(Sub.__bases__)
# print(Super.__bases__)
# x.hello()
# print(x.__dict__)
# x.hola()
# print(x.__dict__)
# print(list(Sub.__dict__.keys()))
# print(list(Super.__dict__.keys()))
# print(x.data1, x.__dict__['data1'])
# x.data3 = 'toast'
# print(x.__dict__)
# print(dir(x))

# class Emp: pass
# class Person(Emp): pass
# bob = Person()
# import classtree
# classtree.instancetree(bob)

# import docstr
# help(docstr)

# class Tmp:
#     x=1
# print(Tmp.x)
# this will be shared by all instances;
# but data attributes are not callable method functions
# redefine subclass __init__ : Superclass.__init__(self, ...)
# redefine subclass method: Superclass.method(self, ...)
# A class is a local scope and has access to enclosing local scopes,
# but it does not serve as an enclosing local scope to further nested code.

# class Number:
#     def __init__(self, start):
#         self.data = start
#     def __sub__(self, other):
#         return Number(self.data - other)
# x = Number(5)
# y = x-3
# print(y.data) # 2

# class Indexer:
#     data = [5, 6, 7, 8, 9]
#     def __getitem__(self, index):
#         return self.data[index]
# x=Indexer()
# print(x[2:4])

# class StepperIndex:
#     def __getitem__(self, i):
#         return self.data[i]
# x=StepperIndex()
# x.data='spam'
# for item in x: print(item)

# class C:
#     def __index__(self):
#         return 255
# x=C()
# print(hex(x))

# class Squares:
#     def __init__(self, start, stop):
#         self.value = start - 1
#         self.stop = stop
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.value == self.stop:
#             raise StopIteration
#         self.value += 1
#         return self.value ** 2
# for i in Squares(1,5): print(i, end=' ')
# x=Squares(1,5)
# print()
# print(next(x)) # 1
# print(next(x)) # 4
# i=iter(x)
# print(next(i)) # 9
# print(next(i)) # 16
# print(next(i)) # 25
# print(tuple(x))     # exhausted
# print()

# def gsquares(start, stop):
#     for i in range(start, stop + 1):
#         yield i ** 2 # generator function (produce iterable objects and retain local variable state)
# for i in gsquares(1, 5):
# #for i in (x ** 2 for x in range(1, 6)):   # the same with generator expression
#     print(i, end=' ')

# class Squares2:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#     def __iter__(self):
#         for value in range(self.start, self.stop + 1):
#             yield value ** 2
# for i in Squares2(1, 5): print(i, end=' ')
# print()
# s=Squares2(1,5)
# i=iter(s)
# print(next(i)) # 1
# print(next(i)) # 4
# j=iter(s)
# print(next(j)) # 1
# print(next(i)) # 9

# class Iters:
#     def __init__(self, value):
#         self.data = value
#     def __contains__(self, x):
#         print('contains: ', end='')
#         return x in self.data
#     def __iter__(self):
#         for x in self.data:
#             yield x
#             print('next:', end='')
#     def __getitem__(self, i):
#         print(f'get:{i} ', end='')
#         return self.data[i]
# if __name__ == '__main__':
#     X = Iters([1, 2, 3, 4, 5])
#     print(3 in X)
#     for i in X: print(i, end='|')
#     print()
#     print([i ** 2 for i in X])
#     print(list(map(bin, X)))
#     I = iter(X)
#     while True:
#         try:
#             print(next(I), end=' @ ')
#         except StopIteration:
#             break

# __getattr__ - intercept non-existence attribute
# __getattribute__ - all attribute
# getattr() - get object's' properties

# class Foo:
#     def __init__(self, x):
#         self.x = x
# f = Foo(10)
# print(getattr(f, 'y', 1))

# class Adder:
#     def __init__(self, value=0):
#         self.data = value
#     def __add__(self, other):
#         #self.data += other
#         print(f'Summing {self} + {other}')
#         return Adder(self.data+other)
# x=Adder()
# print(x, x.data+1)
# class Addrepr(Adder):
#     def __repr__(self):
#         return f'Addrepr({self.data})'
# y = Addrepr(2)
# #y.__add__(1)
# print(y+1)
# class Addstr(Adder):
#     def __str__(self):
#         return f'[Value: {self.data}]'
# z=Addstr(3)
# z.__add__(1)
# print(z, str(z), repr(z))

# class Printer:
#     def __init__(self, val):
#         self.val = val
#     def __repr__(self): # __repr__ used by print if no __str__
#         return str(self.val) # __repr__ used if echoed or nested
# objs = [Printer(2), Printer(3)]
# for x in objs: print(x) # No __str__: runs __repr__
# print(objs) # Runs __repr__, not ___str__

# class Commuter5:
#     def __init__(self, val):
#         self.val = val
#     def __add__(self, other):
#         if isinstance(other, Commuter5):
#             other = other.val
#         return Commuter5(self.val + other)
#     def __radd__(self, other):
#         return Commuter5(other + self.val)
#     def __iadd__(self, other):
#         self.val += other
#         return self
#     def __str__(self):
#         return f'Commuter5: {self.val}'
# x = Commuter5(1)
# y = Commuter5(9)
# print(2+x+y+x+5)
# x+=1
# print(x)

# class Callee:
#     def __call__(self, *pargs, **kargs):
#         print('Called:', pargs, kargs)
# C = Callee()
# C(1, 2, 3, x=4, y=5)
# X = Callee()
# X(1, *(2,), c=3, **dict(d=4))

# class C:
#     data = 'abc'
#     def __gt__(self, other):
#         return self.data > other
#     def __lt__(self, other):
#         return self.data < other
# X = C()
# print(X > 'ab') # True
# print(X > 'abcd') # False


# class Commuter2:
#     def __init__(self, val):
#         self.val = val
#     def __add__(self, other):
#         print('add', self.val, other)
#         return self.val + other
#     def __radd__(self, other):
#         return self.__add__(other)
#         # return self + other   #v2
#     # __radd__ = __add__    # instead of __radd__
#
# class Commuter5:
#     def __init__(self, val):
#         self.val = val
#     def __add__(self, other):
#         if isinstance(other, Commuter5):
#             other = other.val
#         return Commuter5(self.val + other)
#     def __radd__(self, other):
#         return Commuter5(other + self.val)
#     def __str__(self):
#         return '<Commuter5: %s>' % self.val

# class Number:   # +=
#     def __init__(self, val):
#         self.val = val
#     def __iadd__(self, other):
#         self.val += other
#         return self

# class Callee:
#     def __call__(self, *pargs, **kargs):
#         print('Called:', pargs, kargs)
# с=Callee()
# с(1, 2, 3, x=4, y=5)
# с(1, *(2,), c=3, **dict(d=4))
# class Prod:
#     def __init__(self, value):
#         self.value = value
#     def __call__(self, other):
#         return self.value * other
# x=Prod(2)
# print(x(3))    # 6 -- object as function

# class Callback:
#     def __init__(self, color): # Function + state information
#         self.color = color
#     def __call__(self): # Support calls with no arguments
#         print('turn', self.color)
# cb1 = Callback('blue')
# cb1()
# # similar closure variant with 2 def
# def callback(color):
#     def oncall():
#         print('turn', color)
#     return oncall
# cb3 = callback('yellow')
# cb3()

# class C:
#     data = 'spam'
#     def __gt__(self, other):
#         return self.data > other
#     def __lt__(self, other):
#         return self.data < other
# x = C()
# print(x > 'ham')
# print(x < 'ham')

# class Truth:
#     def __bool__(self): return True # 3.X tries __bool__ first
#     def __len__(self): return 0 # 2.X tries __len__ first
# x = Truth()
# if x: print('yes!')

# iteration --> __getitem__ and __iter__
# first: __iter__ + __next__
# if no __iter__ is found: __getitem__ = yield + __next__
#
# __str__ is called by print() and str(), user friendly
# __repr__ - print+str+repr if no __str__ is defined, more details
#
# slicing --> __getitem__
#
# += __iadd__ first, __add__ second

#---------Designing with Classes---------

# class Employee:
#     def __init__(self, name, salary=0):
#         self.name = name
#         self.salary = salary
#     def giveRaise(self, percent):
#         self.salary = self.salary + (self.salary * percent)
#     def work(self):
#         print(self.name, "does stuff")
#     def __repr__(self):
#         return "<Employee: name=%s, salary=%s>" % (self.name, self.salary)
# class Chef(Employee):
#     def __init__(self, name):
#         Employee.__init__(self, name, 50000)
#     def work(self):
#         print(self.name, "makes food")
# class Server(Employee):
#     def __init__(self, name):
#         Employee.__init__(self, name, 40000)
#     def work(self):
#         print(self.name, "interfaces with customer")
# class PizzaRobot(Chef):
#     def __init__(self, name):
#         Chef.__init__(self, name)
#     def work(self):
#         print(self.name, "makes pizza")
# class Customer:
#     def __init__(self, name):
#         self.name = name
#     def order(self, server):
#         print(self.name, "orders from", server)
#     def pay(self, server):
#         print(self.name, "pays for item to", server)
# class Oven:
#     def bake(self):
#         print("oven bakes")
# class PizzaShop:
#     def __init__(self):
#         self.server = Server('Pat') # Embed other objects
#         self.chef = PizzaRobot('Bob') # A robot named bob
#         self.oven = Oven()
#     def order(self, name):
#         customer = Customer(name) # Activate other objects
#         customer.order(self.server)
#         self.chef.work()
#         self.oven.bake()
#         customer.pay(self.server)
# if __name__ == "__main__":
#     scene = PizzaShop() # Make the composite
#     scene.order('Homer') # Simulate Homer's order
#     print('...')
#     scene.order('Shaggy')
# shop = PizzaShop()
# print(shop.server, shop.chef)
# import pickle
# pickle.dump(shop, open('shopfile.pkl', 'wb'))
# obj = pickle.load(open('shopfile.pkl', 'rb'))
# print(obj.server, obj.chef)
# obj.order('Lenin')

# class Processor:
#     def __init__(self, reader, writer):
#         self.reader = reader
#         self.writer = writer
#     def process(self):
#         while True:
#             data = self.reader.readline()
#             if not data: break
#             data = self.converter(data)
#             self.writer.write(data)
#     def converter(self, data):
#         assert False, 'converter must be defined'
# class Uppercase(Processor):
#     def converter(self, data):
#         return data.upper()
# class HTMLize:
#     def write(self, line):
#         print('<PRE>%s</PRE>' % line.rstrip())
# if __name__ == '__main__':
#     import sys
#     obj = Uppercase(open('tst.txt'), sys.stdout)
#     obj.process()
#     print()
#     Uppercase(open('tst.txt'), HTMLize()).process()

# class Wrapper:
#     def __init__(self, object):
#         self.wrapped = object # Save object
#     def __getattr__(self, attrname):
#         print('Trace: ' + attrname) # Trace fetch
#         return getattr(self.wrapped, attrname)
# x = Wrapper([1, 2, 3])
# x.append(4)
# print(x.wrapped)
# x = Wrapper({'a': 1, 'b': 2})
# print(x.keys())

# class Tool:
#     def __method(self): ... # Becomes _Tool__method

# class Spam:
#     def doit(self, message):
#         print(message)
#     def selfless(arg1, arg2):  # A simple function in 3.X
#         return arg1 + arg2
# object1 = Spam()
# object1.doit('hello')   # standard
# x = object1.doit    # bound method - combine an instance and a method function;
# x('hello')
# y = Spam.doit   # unbound method
# y(object1, 'howdy')
# print(Spam.selfless(3, 4))

# def factory(aClass, *pargs, **kargs):
#     return aClass(*pargs, **kargs)
# class Spam:
#     def doit(self, message):
#         print(message)
# class Person:
#     def __init__(self, name, job=None):
#         self.name = name
#         self.job = job
# object1 = factory(Spam)
# object2 = factory(Person, "Arthur", "King")
# object3 = factory(Person, name='Brian')
# object1.doit(99)
# print(object2.job)
# print(object3.name)

# class ListInstance:
#     """
#     Mix-in class that provides a formatted print() or str() of instances via
#     inheritance of __str__ coded here; displays instance attrs only; self is
#     instance of lowest class; __X names avoid clashing with client's attrs
#     """
#     def __attrnames(self):
#         result = ''
#         # for attr in sorted(self.__dict__):
#         for attr in dir(self):
#             if attr[:2] == '__' and attr[-2:] == '__':
#                 result += f'\t{attr}\n'
#             else:
#                 result += f'\t{attr}={getattr(self, attr)}\n'
#         return result
#     def __str__(self):
#         return (f'<Instance of {self.__class__.__name__},'
#                 f' address {id(self)}:'
#                 f' {self.__attrnames()}>')
# class Spam(ListInstance):
#     def __init__(self):
#         self.data1 = 'food'
# x = Spam()
# print(x)
# # print(repr(x))
# class Super:
#     def __init__(self):
#         self.data1 = 'spam'
#     def ham(self):
#         pass
# class Sub(Super, ListInstance):
#     def __init__(self):
#         Super.__init__(self)
#         self.data2 = 'eggs'
#         self.data3 = 42
#     def spam(self):
#         pass
# y = Sub()
# print(y)

# #delegation example
# class A:
#   def spam(self, x):
#     print(‘A.spam’, x)
#   def foo(self):
#     print(‘A.foo’)
# class B:    # class B(A): - inheritance
#   def __init__(self):
#     self._a = A()
#   def spam(self, x):
#     print(‘B.spam’, x)
#     self._a.spam(x)
#   def bar(self):
#     print('B.bar')
#   def __getattr__(self, name):  # use __getattr__
#     return getattr(self._a, name)

# class Set(list):
#     def __init__(self, value=[]): # Constructor
#         list.__init__([]) # Customizes list
#         self.concat(value)
#     def intersect(self, other):  # other is any sequence
#         res = []  # self is the subject
#         for x in self:
#             if x in other:  # Pick common items
#                 res.append(x)
#         return Set(res)  # Return a new Set
#     def union(self, other):  # other is any sequence
#         res = Set(self)  # Copy me and my list
#         res.concat(other)
#         return res
#     def concat(self, value):  # value: list, Set, etc.
#         for x in value:  # Removes duplicates
#             if not x in self:
#                 self.append(x)
#     def __and__(self, other): return self.intersect(other)
#     def __or__(self, other): return self.union(other)
#     def __repr__(self): return 'Set:' + list.__repr__(self)
# if __name__ == '__main__':
#     x = Set([1,3,5,7])
#     y = Set([2,1,4,5,6])
#     print(x, y, len(x))
#     print(x.intersect(y), y.union(x))
#     print(x & y, x | y)
#     x.reverse(); print(x)

# class C(object): # New-style: 3.X and 2.X
#     data = 'spam'
#     def __getattr__(self, name): # Catch normal names
#         print('getattr: ' + name)
#         return getattr(self.data, name)
#     def __getitem__(self, i): # Redefine built-ins
#         print('getitem: ' + str(i))
#         return self.data[i] # Run expr or getattr
#     def __add__(self, other):
#         print('add: ' + other)
#         return getattr(self.data, '__add__')(other)
# x=C()
# print(x.upper())
# print(x[1])
# print(x+'maps')

# #DFLR vs MRO - diamonds
# class A: attr = 1
# class B(A): pass
# class C(A): attr = 2    # stop search for attribute
# class D(B, C): pass
# #class D(B, C): attr = B.attr   # Choose A.attr, above = 1
# x = D()
# print(x.attr)   # 2 (MRO)
# print(D.__mro__)  # D-B-C-A-obj

# #MRO - nondiamond [DFLR - depth first then left to right]
# class A: pass
# class B(A): pass # Nondiamonds: order same as classic
# class C: pass # Depth first, then left to right
# class D(B, C): pass
# print(D.__mro__)   # D-B-A-C-obj

# class X: pass
# class Y: pass
# class A(X): pass # Nondiamond: depth first then left to right
# class B(Y): pass # Though implied "object" always forms a diamond
# class D(A, B): pass
# print(D.__mro__)   # D-A-X-B-Y-obj
