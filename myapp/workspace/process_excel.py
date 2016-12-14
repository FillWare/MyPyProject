# !/usr/bin/env python
from openpyxl import load_workbook
import sys
import os


class ExcelProcessor(object):
    def __init__(self, excel_file_name, txt_file_name):
        self.excel_file_name = excel_file_name
        self.txt_file_name = txt_file_name

    def do_process(self):
        count = 0
        if self.excel_file_name and self.txt_file_name:
            try:
                work_book = load_workbook(filename=self.excel_file_name)
                sheet_names = work_book.get_sheet_names()
                sheet_name = sheet_names[0]
                work_sheet = work_book.get_sheet_by_name(sheet_name)

                f = open(self.txt_file_name, 'w')
                rows = work_sheet.rows
                for row in rows:
                    count += 1
                    # skip title
                    if count == 1:
                        continue
                    line = [column.value for column in row]
                    if len(line) >= 3:
                        f.write(",".join([line[0], line[2], line[1]]) + os.linesep)
            except Exception, e:
                print 'unexpected error:', e


def main():
    if len(sys.argv) < 2:
        print 'Usage: python %s <*.xlsx> <*.txt>' % sys.argv[0]
    else:
        processor = ExcelProcessor(sys.argv[1], sys.argv[2])
        processor.do_process()


if __name__ == "__main__":
    main()
