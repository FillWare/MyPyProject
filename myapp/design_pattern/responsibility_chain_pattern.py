#!/usr/bin/env python
# coding=utf-8


def print_info(info):
    print info


class Manager(object):
    successor = None
    name = ''

    def __init__(self, name):
        self.name = name

    def set_successor(self, successor):
        self.successor = successor

    def handle_request(self, request):
        pass


class CommonManager(Manager):
    def handle_request(self, request):
        if request.request_type == '请假' and request.num <= 2:
            print "{}:{} 数量{} 被批准".format(self.name, request.request_content, request.num)
        else:
            if self.successor is not None:
                self.successor.handle_request(request)


class Majordomo(Manager):
    def handle_request(self, request):
        if request.request_type == '请假' and request.num <= 5:
            print "{}:{} 数量{} 被批准".format(self.name, request.request_content, request.num)
        else:
            if self.successor is not None:
                self.successor.handle_request(request)


class GeneralManager(Manager):
    def handle_request(self, request):
        if request.request_type == '请假':
            print "{}:{} 数量{} 被批准".format(self.name, request.request_content, request.num)
        elif request.request_type == '加薪' and request.num <= 500:
            print "{}:{} 数量{} 被批准".format(self.name, request.request_content, request.num)
        elif request.request_type == '加薪' and request.num > 500:
            print "{}:{} 数量{} 再说吧".format(self.name, request.request_content, request.num)


class Request(object):
    request_type = ''
    request_content = ''
    num = 0


def client():
    common_manager = CommonManager('common-manager')
    majordomo = Majordomo("majordomo")
    general_manager = GeneralManager("general-manager")

    common_manager.set_successor(majordomo)
    majordomo.set_successor(general_manager)

    request = Request()
    request.request_type = '请假'
    request.request_content = '小菜请假'
    request.num = 1
    common_manager.handle_request(request)

    request.num = 5
    common_manager.handle_request(request)

    request.request_type = '加薪'
    request.request_content = '小菜要求加薪'
    request.num = 500
    common_manager.handle_request(request)

    request.num = 1000
    common_manager.handle_request(request)


if __name__ == '__main__':
    client()
