class SimpleDecor(object):

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __call__(self, f):
        def wrapped_f(*args, **kwargs):
            print("Args to class {}".format(self.args))
            print("K-Args to class ({})".format(' '.join('%s=%s' % (k, v) for k, v in self.kwargs.items())))
            #Do something here
            print("Args to fuction ({})".format(args))
            print("K-Args to fuction ({})".format(' '.join('%s=%s' % (k, v) for k, v in kwargs.items())))
            return f(*args, **kwargs)
        return wrapped_f


@SimpleDecor('This', 'is', 'class', 'argument', version=1)
def sayHello(fname, lastname, age, initial):
    return '{} {} {} is {} year old'.format(initial, fname, lastname, age)


print(sayHello('Abc', 'Xyz', initial='Mr', age =90))