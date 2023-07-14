def fun(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


def fun2(*args, **kwargs):
    print(args)
    print(kwargs)


fun(a=10, b=20, x=1)
fun(name='Abc', age=30)
fun2(10, 20, a=1, b=2)
