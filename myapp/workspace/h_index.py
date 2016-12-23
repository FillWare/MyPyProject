#!/usr/bin/env python

LINE_SEP = "*" * 20


class Solution(object):
    def __init__(self, citations):
        self.__citations = citations

    def get_h_index(self):
        ret = 0
        if self.__citations:
            self.__citations.sort()
            sz = len(self.__citations)
            for index, item, in enumerate(self.__citations):
                if item != 0 and item >= (sz - index):
                    ret = sz - index
                    break
        return ret

    def set_citations(self, citations):
        self.__citations = citations


def main():
    print LINE_SEP
    citations = [0]
    s = Solution(citations)
    print s.get_h_index()
    print LINE_SEP
    citations = [1]
    s.set_citations(citations)
    print s.get_h_index()
    print LINE_SEP
    citations = [100]
    s.set_citations(citations)
    print s.get_h_index()
    print LINE_SEP
    citations = [3, 0, 6, 5, 1]
    s.set_citations(citations)
    print s.get_h_index()
    print LINE_SEP
    citations = [5, 6, 10, 20, 35]
    s.set_citations(citations)
    print s.get_h_index()


if __name__ == '__main__':
    main()