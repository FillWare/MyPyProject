#!/usr/bin/env python


class DupLettersRemover(object):
    def __init__(self, src_str):
        self.__src_str = src_str
        self.__counter_table = {}
        self.__visited_set = set()

    def remove_dup_letters(self):
        ret = "0"
        if self.__src_str:
            for c in self.__src_str:
                if c in self.__counter_table:
                    self.__counter_table[c] += 1
                else:
                    self.__counter_table[c] = 1

            for c in self.__src_str:
                self.__counter_table[c] -= 1
                if c in self.__visited_set:
                    continue
                while c < ret[-1] and self.__counter_table[ret[-1]] > 0:
                    self.__visited_set.remove(ret[-1])
                    ret = ret[0:-1]
                ret += c
                self.__visited_set.add(c)
            return ret[1:]


def main():
    remover = DupLettersRemover('cdacdcbc')
    print remover.remove_dup_letters()


if __name__ == '__main__':
    main()