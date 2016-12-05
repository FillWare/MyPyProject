#!/usr/bin/env python
# coding=utf-8


class Director(object):
    def __init__(self):
        self.builder = None

    def construct_building(self):
        self.builder.new_building()
        self.builder.build_floor()
        self.builder.build_size()

    def get_building(self):
        return self.builder.building


class Builder(object):
    def __init__(self):
        self.building = None

    def new_building(self):
        self.building = Building()

    def build_floor(self):
        raise NotImplementedError

    def build_size(self):
        raise NotImplementedError


class BuildHouse(Builder):
    def build_floor(self):
        self.building.floor = "One"

    def build_size(self):
        self.building.size = "Big"


class BuildFlat(Builder):
    def build_floor(self):
        self.building.floor = "More than one"

    def build_size(self):
        self.building.size = "Small"


class Building(object):
    def __init__(self):
        self.floor = None
        self.size = None

    def __repr__(self):
        return "Floor:{0.floor} | Size:{0.size}".format(self)

    __str__ = __repr__


def main():
    director = Director()

    director.builder = BuildHouse()
    director.construct_building()
    print director.get_building()

    director.builder = BuildFlat()
    director.construct_building()
    print director.get_building()


if __name__ == '__main__':
    main()