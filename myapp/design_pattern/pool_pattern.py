#!/usr/bin/env python


class QueueObject(object):
    def __init__(self, queue, auto_get=False):
        self._queue = queue
        self.object = self._queue.get() if auto_get else None

    def __enter__(self):
        if self.object is None:
            self.object = self._queue.get()
        return self.object

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.object is not None:
            print self.object + " in __exit__"
            self._queue.put(self.object)
            self.object = None
        return

    def __del__(self):
        if self.object is not None:
            print self.object + " in __del__"
            self._queue.put(self.object)
            self.object = None
        return


def main():
    try:
        import queue
    except ImportError:
        import Queue as queue

    def test_object(queue):
        queue_obj = QueueObject(queue, True)
        print "Inside function:{}".format(queue_obj.object)

    sample_queue = queue.Queue()
    sample_queue.put("yam")
    with QueueObject(sample_queue) as obj:
        print "Inside with:{}".format(obj)
    print "Outside with:{}".format(sample_queue.get())

    sample_queue.put("sam")
    test_object(sample_queue)
    print "Outside function:{}".format(sample_queue.get())

    if not sample_queue.empty():
        print sample_queue.get()


if __name__ == "__main__":
    main()
