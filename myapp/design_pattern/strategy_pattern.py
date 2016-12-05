#!/usr/bin/env python
import types


class StrategyExample(object):
    def __init__(self, method=None):
        self.name = "Strategy example 0"
        if method is not None:
            self.execute = types.MethodType(method, self)

    def execute(self):
        print self.name


def execute_replacement_one(self):
    print "{self.name} from execute one".format(self=self)


def execute_replacement_two(self):
    print "{self.name} from execute two".format(self=self)


def main():
    strategy0 = StrategyExample()
    strategy1 = StrategyExample(execute_replacement_one)
    strategy1.name = "Strategy example 1"
    strategy2 = StrategyExample(execute_replacement_two)
    strategy2.name = "Strategy example 2"
    strategy0.execute()
    strategy1.execute()
    strategy2.execute()


if __name__ == '__main__':
    main()
