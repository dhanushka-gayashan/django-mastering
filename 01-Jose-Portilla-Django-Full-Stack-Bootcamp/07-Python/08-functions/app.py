def my_func(param1='default'):
    """
    This is first function
    :param param1: name of writer
    :return: nothing
    """
    return "my first python function!! {}".format(param1)


welcome = my_func('Dhanushka')
print(welcome)


def add_param(num1, num2):
    return num1 + num2


print(add_param(10, 20))
print(add_param("10", "20"))


def add_num(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        return num1 + num2
    else:
        return 'Sorry, I need integers!'


result = add_num('10', '20')
print(result)

result = add_num(10, 20)
print(result)


myList = range(10)
evens = filter(lambda num: num % 2 == 0, myList)
print(list(evens))


print('x' in [1, 2, 3])
print(2 in [1, 2, 3])