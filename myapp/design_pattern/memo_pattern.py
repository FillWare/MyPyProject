#!/usr/bin/env python
from copy import copy, deepcopy


def do_memo(obj, deep=False):
    state = deepcopy(obj.__dict__) if deep else copy(obj.__dict__)

    def restore():
        obj.__dict__.clear()
        obj.__dict__.update(state)

    return restore


class Transaction(object):
    deep = False
    states = []

    def __init__(self, deep, *targets):
        self.deep = deep
        self.targets = targets
        self.commit()

    def commit(self):
        self.states = [do_memo(target, self.deep) for target in self.targets]

    def rollback(self):
        for a_state in self.states:
            a_state()


class Transactional(object):
    def __init__(self, method):
        self.method = method

    def __get__(self, obj, T):
        def transactions(*args, **kwargs):
            state = do_memo(obj)
            try:
                return self.method(obj, *args, **kwargs)
            except Exception as e:
                state()
                raise e

        return transactions


class NumObj(object):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return "<{}: {}>".format(self.__class__.__name__, self.value)

    def incremental(self):
        self.value += 1

    @Transactional
    def do_stuff(self):
        self.value = "1111"
        self.incremental()

    __str__ = __repr__


def main():
    num_obj = NumObj(-1)
    print num_obj
    a_transaction = Transaction(True, num_obj)

    try:
        for i in range(3):
            num_obj.incremental()
            print num_obj
        a_transaction.commit()
        print '-- committed'

        for i in range(3):
            num_obj.incremental()
            print num_obj
        num_obj += 'x'
        print num_obj
    except Exception as e:
        a_transaction.rollback()
        print '-- rollback'
    print num_obj

    print '-- now doing stuff --'
    try:
        num_obj.do_stuff()
    except Exception as e:
        print '-> doing stuff failed!'
        import sys
        import traceback

        traceback.print_exc(file=sys.stdout)
    print num_obj


if __name__ == '__main__':
    main()
