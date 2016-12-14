# !/usr/bin/env python
# -*-coding:utf-8-*-

import time
import sys
import random

# globals
ips = ['83.149.9.216', '93.114.45.13', '46.105.14.53', '110.136.166.128', '200.49.190.101', '66.249.73.135']
fake_time = "[2015-01-04T%02d:%02d:%02d.000Z]"
body = '"GET /blog/tags/web HTTP/1.1" 200' + " %d " + '"-" "QS304 Profile/MIDP-2.0 Configuration/CLDC-1.1"'


class MyFileWriter(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.count = 0

    def write_to_file_interval_in_sec(self, interval):
        if self.file_name is None:
            print 'No file got.\n'
            return

        if interval is None:
            interval = 2

        f = None
        try:
            f = open(self.file_name, 'a')
        except Exception, ex:
            print ex
            if f is not None:
                f.close()
            return

        while True:
            try:
                words = [random.choice(ips), '-', '-',
                         fake_time % (random.randint(0, 23), random.randint(0, 59), random.randint(0, 59)),
                         body % (random.randint(0, 10000)), '\n']
                pattern = ' '.join(words)
                pattern.strip()
                print 'adding line {}: {}\n'.format(self.count, pattern)
                self.count += 1
                f.write(pattern)
                f.flush()
            except Exception, ex:
                print ex
                f.close()
                break

            try:
                time.sleep(interval)
            except Exception, ex:
                print ex

        f.close()
        return


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage: python <%s> <file path>\n" % sys.argv[0]
    else:
        print 'writing to file: %s\n' % sys.argv[1]
        fileWriter = MyFileWriter(sys.argv[1])
        fileWriter.write_to_file_interval_in_sec(2)
