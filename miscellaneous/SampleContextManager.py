
class Divisor(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def divide(self):
        return self.x/self.y

    def __str__(self):
        return "Divisor(" + str(self.x) + "," + str(self.y) + ")"


class SampleContextManager(object):

    def __init__(self, a, b):
        self.file_obj = Divisor(a, b)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, error_type, error_value, traceback):
        print ("I have been called for " + str(self.file_obj) + " with object ref " + self.file_obj.__repr__())

# Alternative of defining class


from contextlib import contextmanager


@contextmanager
def context_manager_generator(a, b):
    d = Divisor(a, b)
    try:
        yield d
    except Exception, e:
        print e
    print ("I have been called for " + str(d) + " with object ref " + d.__repr__())


if __name__ == '__main__':

    with SampleContextManager(4, 1) as s:
        s.divide()

    with context_manager_generator(4, 0) as s:
        print s.divide()





