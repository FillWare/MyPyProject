#!/usr/bin/env python
# -*-coding : utf-8-*-


class DataNode(object):
    def __init__(self, key, value, freq, pre_node, next_node):
        self.key = key
        self.value = value
        self.freq = freq
        self.next_node = next_node
        self.pre_node = pre_node


class FreqNode(object):
    def __init__(self, freq, pre_node, next_node):
        self.freq = freq
        self.next_node = next_node
        self.pre_node = pre_node
        self.head = self.tail = None


class LFUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = FreqNode(0, None, None)
        self.data_map = {}
        self.freq_map = {}

    def get(self, key):
        if key in self.data_map:
            data_node = self.data_map.get(key)
            freq_node = self.freq_map.get(data_node.freq)
            data_node.freq += 1
            next_freq_node = freq_node.next_node
            if not next_freq_node or next_freq_node.freq > data_node.freq:
                next_freq_node = FreqNode(data_node.freq, freq_node, freq_node.next_node)
                self.freq_map[next_freq_node.freq] = next_freq_node
                self.__insert_freq_node_after(freq_node, next_freq_node)
            self.__unlink_data_node(data_node, freq_node)
            self.__link_data_node(data_node, next_freq_node)
            return data_node.value
        return -1

    def set(self, key, value):
        if key in self.data_map:
            data_node = self.data_map.get(key)
            freq_node = self.freq_map.get(data_node.freq)
            data_node.freq += 1
            next_freq_node = freq_node.next_node
            data_node.value = value
            if not next_freq_node or next_freq_node.freq > data_node.freq:
                next_freq_node = FreqNode(data_node.freq, freq_node, freq_node.next_node)
                self.freq_map[next_freq_node.freq] = next_freq_node
                self.__insert_freq_node_after(freq_node, next_freq_node)
            self.__unlink_data_node(data_node, freq_node)
            self.__link_data_node(data_node, next_freq_node)
        else:
            if self.capacity == 0:
                return
            if self.capacity == len(self.data_map):
                self.__remove_data_node(self.head.next_node)
            data_node = DataNode(key, value, 1, None, None)
            self.data_map[data_node.key] = data_node
            freq_node = self.freq_map.get(data_node.freq)
            if not freq_node:
                freq_node = FreqNode(data_node.freq, self.head, self.head.next_node)
                self.freq_map[freq_node.freq] = freq_node
                self.__insert_freq_node_after(self.head, freq_node)
            self.__link_data_node(data_node, freq_node)

    def __unlink_data_node(self, data_node, freq_node):
        if not data_node or not freq_node:
            return
        pre_data_node = data_node.pre_node
        next_data_node = data_node.next_node
        if pre_data_node:
            pre_data_node.next_node = next_data_node
        else:
            freq_node.head = next_data_node
        if next_data_node:
            next_data_node.pre_node = pre_data_node
        else:
            freq_node.tail = pre_data_node
        if not freq_node.head:
            self.__remove_freq_node(freq_node)

    def __link_data_node(self, data_node, freq_node):
        if not data_node or not freq_node:
            return
        data_node.next_node = freq_node.head
        if freq_node.head:
            freq_node.head.pre = data_node
        freq_node.head = data_node
        if not freq_node.tail:
            freq_node.tail = data_node

    def __remove_freq_node(self, freq_node):
        if not freq_node:
            return
        next_freq_node = freq_node.next_node
        if next_freq_node:
            next_freq_node.pre_node = freq_node.pre_node
        freq_node.pre_node.next_node = next_freq_node
        del self.freq_map[freq_node.freq]

    def __insert_freq_node_after(self, node, new_node):
        if not node or not new_node:
            return
        node.next_node = new_node
        if new_node.next_node:
            new_node.next_node.pre_node = new_node

    def __remove_data_node(self, freq_node):
        if not freq_node:
            return
        tail_data_node = freq_node.tail
        pre_data_node = tail_data_node.pre_node
        if pre_data_node:
            freq_node.tail = pre_data_node
        else:
            freq_node.head = tail_data_node.next_node
        if not freq_node.head:
            self.__remove_freq_node(freq_node)


def main():
    cache = LFUCache(10)
    cache.set(1, 2)
    print cache.get(1)
    cache.set(1, 5)
    print cache.get(1)
    cache.set('key1', 7)
    print cache.get('key1')

if __name__ == '__main__':
    main()