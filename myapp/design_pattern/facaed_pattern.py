#!/usr/bin/env python
import time

SLEEP = 0.5
PONDER = 6
SEPARATOR = " ".join(['#' * PONDER, "In Test {}", '#' * PONDER])


class TC1(object):
    def run(self):
        print SEPARATOR.format(1)
        time.sleep(SLEEP)
        print "Setting up"
        time.sleep(SLEEP)
        print "Running test"
        time.sleep(SLEEP)
        print "Tearing down"
        time.sleep(SLEEP)
        print "Test finished\n"


class TC2(object):
    def run(self):
        print SEPARATOR.format(2)
        time.sleep(SLEEP)
        print "Setting up"
        time.sleep(SLEEP)
        print "Running test"
        time.sleep(SLEEP)
        print "Tearing down"
        time.sleep(SLEEP)
        print "Test finished\n"


class TC3(object):
    def run(self):
        print SEPARATOR.format(3)
        time.sleep(SLEEP)
        print "Setting up"
        time.sleep(SLEEP)
        print "Running test"
        time.sleep(SLEEP)
        print "Tearing down"
        time.sleep(SLEEP)
        print "Test finished\n"


class TestRunner(object):
    def __init__(self):
        self.tc1 = TC1()
        self.tc2 = TC2()
        self.tc3 = TC3()
        self.tests = (self.tc1, self.tc2, self.tc3)

    def run_all(self):
        [i.run() for i in self.tests]


def client():
    test_runner = TestRunner()
    test_runner.run_all()


if __name__ == '__main__':
    client()
