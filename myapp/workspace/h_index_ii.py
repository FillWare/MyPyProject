#!/usr/bin/env python
# -*-coding : utf8-*-


class Solution(object):
    def h_index_ii(self, citations):
        if not citations:
            return 0

        sz = len(citations)
        start = 0
        end = sz - 1
        while start <= end:
            mid = (start + end) / 2
            if citations[mid] < sz - mid:
                start = mid + 1
            else:
                end = mid - 1
        return sz - start


def main():
    s = Solution()
    citations = [5, 6, 7, 8, 9]
    print s.h_index_ii(citations)


if __name__ == '__main__':
    main()
