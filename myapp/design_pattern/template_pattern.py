#!/usr/bin/env python

ingredients = "spam eggs apple"
line = "-" * 10


def iter_items(getter, action):
    for item in getter():
        action(item)
        print line


def rev_items(getter, action):
    for item in reversed(getter()):
        action(item)
        print line


def get_list():
    return ingredients.split()


def get_lists():
    return [list(x) for x in ingredients.split()]


def print_item(item):
    print item


def reverse_item(item):
    print item[::-1]


def make_template(skeleton, getter, action):
    def template():
        skeleton(getter, action)
    return template


def main():
    templates = [make_template(s, g, a)
                 for g in (get_list, get_lists)
                 for a in print_item, reverse_item
                 for s in (iter_items, rev_items)]
    for template in templates:
        template()


if __name__ == '__main__':
    main()