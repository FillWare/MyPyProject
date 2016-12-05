#!/usr/bin/env python
# coding=utf-8
import time


class SalesManager(object):
    def work(self):
        print "Sales manager is working"

    def talk(self):
        print "Sales manager is ready to talk"


class Proxy(object):
    def __init__(self):
        self.busy = 'No'
        self.sales = None

    def work(self):
        print "Proxy checking for Sales manager availability"
        if self.busy == 'No':
            self.sales = SalesManager()
            time.sleep(2)
            self.sales.talk()
        else:
            time.sleep(2)
            print "Sales Manager is busy"


class NoTalkProxy(Proxy):
    def __init__(self):
        Proxy.__init__(self)

    def work(self):
        print "Proxy checking for Sales manager availability"
        time.sleep(2)
        print "This sales manager will not talk to you whether she/he is busy or not"


def main():
    p = Proxy()
    p.work()
    p.busy = 'Yes'
    p.work()
    p = NoTalkProxy()
    p.work()
    p.busy = 'Yes'
    p.work()


if __name__ == '__main__':
    main()
