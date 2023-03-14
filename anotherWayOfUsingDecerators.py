# Python code to illustrate
# Decorators with parameters in Python

def decorator_func(x, y):
    print("inside decorator")
    def Inner(func):
        def wrapper(*args, **kwargs):
            print("I like Geeksforgeeks")
            print("Summation of values - {}".format(x + y))

            func(*args, **kwargs)

        return wrapper

    return Inner


# ------------------------Not using decorator-----------------------
def my_fun(*args):
    for ele in args:
        print(ele)


# another way of using decorators
decorator_func(12, 15)(my_fun)('Geeks', 'for', 'Geeks')
