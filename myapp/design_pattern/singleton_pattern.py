#!/usr/bin/env python


class Borg(object):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = "Init"

    def __str__(self):
        return self.state


class YoungBorg(Borg):
    def __init__(self, a):
        Borg.__init__(self)
        self.a = a


def borg(cls):
    cls.__state = {}
    orig_init = cls.__init__

    def new_init(self, *args, **kwargs):
        self.__dict__ = cls.__state
        orig_init(self, *args, **kwargs)

    cls.__init__ = new_init
    return cls


@borg
class MyBorg(object):
    def __init__(self, a):
        self.a = a
        print MyBorg.__dict__


class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance


class MySingleton(object):
    __metaclass__ = Singleton

    def __init__(self, a):
        self.a = a


def main():
    # a = YoungBorg(1)
    # print a.a
    # b = YoungBorg(2)
    # print b.a
    # print a.a
    # print id(a) == id(b)
    # c = MyBorg(1)
    # print c.a
    # d = MyBorg(2)
    # print d.a
    # d.a = 5
    # print c.a
    # e = MySingleton(1)
    # print e.a
    # f = MySingleton(2)
    # print f.a
    # g = MySingleton2(1)
    # print g.a
    # h = MySingleton2(2)
    # print h.a
    factory = SingletonFactory()
    i = factory(MySingleton3, 1)
    print i.a
    j = factory(MySingleton3, 2)
    print j.a


def singleton(cls, *args, **kwargs):
    instances = {}

    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return _singleton


@singleton
class MySingleton2(object):
    def __init__(self, a):
        self.a = a


class SingletonFactory(object):
    instances = {}

    def __call__(self, cls, *args, **kwargs):
        if cls not in self.instances:
            self.instances[cls] = cls(*args, **kwargs)
        return self.instances[cls]


class MySingleton3(object):
    def __init__(self, a):
        self.a = a


if __name__ == '__main__':
    main()
