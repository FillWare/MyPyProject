#!/usr/bin/env python
# coding=utf-8
import copy


class Prototype(object):
    value = "default"

    def clone(self, **attrs):
        obj = copy.deepcopy(self)
        obj.__dict__.update(attrs)
        return obj


class PrototypeDispatcher(object):
    def __init__(self):
        self._objects = {}

    def get_objects(self):
        return self._objects

    def register_object(self, name, value):
        self._objects[name] = value

    def un_register_object(self, name):
        del self._objects[name]


def main():
    dispatcher = PrototypeDispatcher()
    prototype = Prototype()

    d = prototype.clone()
    a = prototype.clone(value='a-value', category="a")
    b = prototype.clone(value='b-value', isChecked=True)
    dispatcher.register_object("object_a", a)
    dispatcher.register_object("object_b", b)
    dispatcher.register_object("default", d)

    print [{n: p.value} for n, p in dispatcher.get_objects().items()]


if __name__ == '__main__':
    main()



