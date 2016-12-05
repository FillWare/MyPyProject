#!/usr/bin/env python
import random
import time


class TC(object):
    def __init__(self):
        self._tm = None
        self.problem = 0

    def setup(self):
        print 'Setting up test'
        time.sleep(0.1)
        self._tm.prepare_reporting()

    def execute(self):
        if not self.problem:
            print 'Executing the test'
            time.sleep(0.1)
        else:
            print 'Problem in setup, Test not executed'

    def tear_down(self):
        if not self.problem:
            print 'Tearing down'
            time.sleep(0.1)
            self._tm.publish_reporting()
        else:
            print 'Test not executed, No tear down required'

    def set_tm(self, tm):
        self._tm = tm

    def set_problem(self, problem):
        self.problem = problem


class Reporter(object):
    def __init__(self):
        self._tm = None

    def prepare(self):
        print 'Reporter class is prepare to report the results'
        time.sleep(0.1)

    def report(self):
        print 'Reporting the results of test'
        time.sleep(0.1)

    def set_tm(self, tm):
        self._tm = tm


class DB(object):
    def __init__(self):
        self._tm = None

    def insert(self):
        print 'Inserting the execution begin status in the Database'
        time.sleep(0.1)
        if random.randrange(1, 4) == 3:
            return -1

    def update(self):
        print 'Updating the test results in Database'
        time.sleep(0.1)

    def set_tm(self, tm):
        self._tm = tm


class TestManager(object):
    def __init__(self):
        self._reporter = None
        self._db = None
        self._tc = None

    def prepare_reporting(self):
        rvalue = self._db.insert()
        if rvalue == -1:
            self._tc.set_problem(1)
            self._reporter.prepare()

    def set_reporter(self, reporter):
        self._reporter = reporter

    def set_db(self, db):
        self._db = db

    def publish_reporting(self):
        self._db.update()
        self._reporter.report()

    def set_tc(self, tc):
        self._tc = tc


def main():
    reporter = Reporter()
    db = DB()
    tm = TestManager()
    tm.set_reporter(reporter)
    tm.set_db(db)
    reporter.set_tm(tm)
    db.set_tm(tm)

    for i in range(3):
        tc = TC()
        tc.set_tm(tm)
        tm.set_tc(tc)
        tc.setup()
        tc.execute()
        tc.tear_down()


if __name__ == '__main__':
    main()