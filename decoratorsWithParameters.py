# Python code to illustrate
# Decorators with parameters in Python

def decorator(*args, **kwargs):
    print("Inside decorator")
    print(args[1])
    print(kwargs['fruit'])

    def inner(func):
        # code functionality here
        print("Inside inner function")
        print("I like", kwargs['like'])

        func()

    # returning inner function
    return inner


@decorator(1234, "pranjal", like="forgetfulness", fruit="Mango")
def my_func(num: int = 45):
    print("Inside actual function")
    print(num)
    print("-------------------------------------------")


@decorator(9876, "Sonowal", like="Truth", fruit="JackFruit")
def your_func(num: int = 1010101):
    print("Get Inspired")
    print(num)
    print("-------------------------------------------")
