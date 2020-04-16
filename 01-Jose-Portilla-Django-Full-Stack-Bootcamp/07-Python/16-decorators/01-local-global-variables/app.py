s = "GLOBAL VARIABLE!"


def func():
    mylocal = 10
    print(locals())
    print(globals()['s'])


func()

