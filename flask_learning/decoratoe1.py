

def bold(fn):
    def inner(*args):
        fn(args)
        print(args[0].upper())
    return inner



@bold
def name(na):
    return na

name("logesh")