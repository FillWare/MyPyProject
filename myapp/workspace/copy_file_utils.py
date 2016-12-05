#!/usr/bin/env python
import os
import re
import sys
import shutil


def match_file_name(file_name):
    """
    Get file name
    :param file_name:
    :return:
    """
    matcher = re.compile(u".*?([0-9]+)(.*)")
    groups = matcher.match(file_name)
    matched_name = ""
    if matcher:
        matched_name = groups.group(1) + groups.group(2)
    return matched_name


def copy(src_file_name, dest_file_name):
    """
    Copy file from src_file to dest_file
    :param src_file_name:
    :param dest_file_name:
    :return:
    """
    try:
        shutil.copy(src_file_name, dest_file_name)
    except Exception, e:
        print e


class FilesCopier(object):
    def __init__(self, src_folder, dest_folder):
        self.src_folder = src_folder
        self.dest_folder = dest_folder

    def do_copy(self):
        if self.src_folder and self.dest_folder:
            for parent, dir_name, file_name in os.walk(self.src_folder):
                for file_item in file_name:
                    real_name = os.path.join(parent, file_item)
                    matched_name = match_file_name(file_item)
                    dest_name = os.path.join(self.dest_folder, matched_name)
                    print "coping %s to %s ..." % (real_name, dest_name)
                    copy(real_name, dest_name)
                    print "done!"


def main():
    if len(sys.argv) < 3:
        print "Usage: python %s <src_folder> <dest_folder>" % sys.argv[0]
    else:
        print "It is going to copy files from %s to %s" % (sys.argv[1], sys.argv[2])
        copier = FilesCopier(sys.argv[1], sys.argv[2])
        copier.do_copy()

if __name__ == '__main__':
    main()