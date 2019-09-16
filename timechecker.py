import time


class Profiler(object):

    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Затрачено времени: {:.3f} сек".format(time.time() - self._startTime))
