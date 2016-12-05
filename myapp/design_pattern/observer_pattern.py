#!/usr/bin/env python


class Subject(object):
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def detach(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError, e:
            pass

    def notify(self):
        for observer in self.observers:
            observer.update(self)


class Data(Subject):
    def __init__(self, name):
        Subject.__init__(self)
        self.name = name
        self._data = 0

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self.notify()


class HexViewer(object):
    def update(self, subject):
        print "HexViewer: Subject %s has data 0x%X" %(subject.name, subject.data)


class DecimalViewer(object):
    def update(self, subject):
        print "DecimalViewer: Subject %s has data %d" %(subject.name, subject.data)


def main():
    data1 = Data('data 1')
    data2 = Data('data 2')
    view1 = HexViewer()
    view2 = DecimalViewer()
    data1.attach(view1)
    data1.attach(view2)
    data2.attach(view1)
    data2.attach(view2)

    print "Setting Data1 = 10"
    data1.data = 10
    print "Setting Data2 = 15"
    data2.data = 15
    print "Setting Data1 = 3"
    data1.data = 3
    print "Setting Data2 = 5"
    data2.data = 5
    print "Detach HexViewer from data1 and data2"
    data1.detach(view1)
    data2.detach(view1)
    print "Setting Data1 = 10"
    data1.data = 10
    print "Setting Data2 = 15"
    data2.data = 15

if __name__ == '__main__':
    main()