#!/usr/bin/env python
# coding=utf-8


class Mark(object):
    def __init__(self, mark):
        self.mark = mark


class Style(object):
    def __init__(self, style):
        self.style = style


class Car(object):
    def __init__(self, mark, style):
        self.mark = mark.mark
        self.style = style.style


def main():
    car = Car(Mark('大众'), Style('两厢'))
    print car.mark


if __name__ == '__main__':
    main()
