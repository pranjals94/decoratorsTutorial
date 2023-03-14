# print("hello world")

# passing functions as objects---------------------
# def f1():
#     print(" Called function f1")
#
#
# def f2(arg):
#     arg()
#
#
# f2(f1)  # pass function f1 as argument in function f2


# -----------------------------------------------------------------------

def func1(func):
    def wrapper():
        print("started")
        func()
        print("ended")
        print("-----------------------decorator wrapper function----------")

    # wrapper() # we can call the wrapper function this way
    return wrapper  # or we can return the wrapper function


def func2():
    print("Hello")


# xyz = func1(func2)  # (function alias_ing) xyz stores the returned wrapper function from func1
# xyz()
# func1(func2)()  # single line for the above two lines


# ---if we want to call the func1 every time another function is called, we can use decorators as below------
@func1
def testfunc():
    print("Test Function")


@func1
def hellocheck():
    print("Hello Check !")


# ---- whenever we call the function testfunc, function func1 is called whose argument is the testfunc -----
# this is the beauty of decorator
testfunc()
hellocheck()
