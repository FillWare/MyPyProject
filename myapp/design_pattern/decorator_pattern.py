#!/usr/bin/env python
from functools import wraps


def make_bold(fn):
    return get_wrapped(fn, "b")


def make_italic(fn):
    return get_wrapped(fn, "i")


def get_wrapped(fn, tag):
    @wraps(fn)
    def wrapped():
        return "<%s>%s<%s>" % (tag, fn(), tag)

    return wrapped


def get_wrapped2(tag):
    def inner(fn):
        def wrapped():
            return "<%s>%s<%s>" % (tag, fn(), tag)
        return wrapped
    return inner


@get_wrapped2("b")
@get_wrapped2("i")
def hello():
    return "Hello world!"


def main():
    print hello()


if __name__ == '__main__':
    main()
