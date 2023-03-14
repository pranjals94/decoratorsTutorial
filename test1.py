def func1():
    print("Inside Global Decorator")

    def wrapper(func):
        print("started")
        func()
        print("ended")
        print("-----------------------decorator wrapper function----------")

    return wrapper


@func1()  # by giving the parenthesis means we are calling the function
def testfunc():  # this function goes to the wrapper function of the decorator function
    print("Test Function")


@func1()  # by giving the parenthesis means we are calling the function
def testfunc1():  # this function goes to the wrapper function of the decorator function
    print("Test Function 1")
