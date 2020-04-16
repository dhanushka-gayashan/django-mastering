# Assing Function into a Variable
def hello(name="Dhanushka"):
    return 'Hello ' + name


my_new_greet = hello
print(my_new_greet("Nimalka"))


# Functions within a Function
def greet(name="Dhanushaka"):
    print("THE GREET() FUNCTION HAS BEEN RUN!")

    def hello():
        return "THIS STRING IS INSIDE HELLO()"

    def welcome():
        return "THIS STRING IS INSIDE WELCOME()"

    print(hello())
    print(welcome())
    print("END OF GREET")


greet("Nimalka")


# Return a Function from a Function
def operations(operation):
    def add(a, b):
        return a + b

    def subs(a, b):
        return a - b

    def multi(a, b):
        return a * b

    def devi(a, b):
        return a // b

    if operation == "add":
        return add
    elif operation == "subs":
        return subs
    elif operation == "multi":
        return multi
    elif operation == "devi":
        return devi
    else:
        return "Invalid Operation"


operation = operations("add")
print(operation(40, 20))

operation = operations("subs")
print(operation(40, 20))

operation = operations("multi")
print(operation(40, 20))

operation = operations("devi")
print(operation(40, 20))


# Function as an Argument
def execute(function, va1, val2):
    print(function(va1, val2))


operation = operations("add")
execute(operation,40, 20)

operation = operations("subs")
execute(operation,40, 20)

operation = operations("multi")
execute(operation,40, 20)

operation = operations("devi")
execute(operation,40, 20)


