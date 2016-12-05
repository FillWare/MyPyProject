#!/usr/bin/env python


def lazy(fn):
    """Decorator that makes a property lazy evaluated"""
    attr_name = "_lazy_" + fn.__name__

    @property
    def _lazy_property(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return _lazy_property


class Person(object):
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    @lazy
    def relatives(self):
        relatives = "Many relatives"
        return relatives


def main():
    john = Person("John", "Coder")
    print "Name: {john.name}, Occupation:{john.occupation}, Relatives:{john.relatives}".format(john=john)


if __name__ == '__main__':
    main()
