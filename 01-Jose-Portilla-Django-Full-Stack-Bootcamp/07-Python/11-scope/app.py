# Local Level
root = lambda x: x ** 2

# Global Level vs Enclosing Function Level
name = "This is a global name"
age = 33


def greet():
    name = "Dhanushka"

    def hello():
        print('Hello ' + name + ', your age ' + str(age))

    hello()


greet()

x = 50


def func(x):
    print('x is: ', x)
    x = 1000
    print('local x changed to: ', x)


func(x)
print(x)


def global_func():
    global x
    x = 2000


print(x)
global_func()
print(x)


def best_func():
    return 3000


print(x)
x = best_func()
print(x)