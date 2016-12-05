#!/usr/bin/env python
# coding=utf-8


class GreekGetter(object):
    def __init__(self):
        self.trans = dict(dog="σκύλος", cat="γάτα")

    def get(self, msg):
        return self.trans.get(msg, str(msg))


class ChineseGetter(object):
    def __init__(self):
        self.trans = dict(dog="狗", cat="猫")

    def get(self, msg):
        return self.trans.get(msg, str(msg))


class EnglishGetter(object):
    def get(self, msg):
        return str(msg)


def get_localizer(language):
    languages = {"English": EnglishGetter, "Greek": GreekGetter, "Chinese": ChineseGetter}
    return languages.get(language, EnglishGetter)()


def main():
    c, g, j = get_localizer("Chinese"), get_localizer("Greek"), get_localizer("Japanese")
    for msg in "dog parrot cat bear".split():
        print c.get(msg), g.get(msg), j.get(msg)


if __name__ == '__main__':
    main()
