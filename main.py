# Python Decorators

# 1. What is a decorator?

# A decorator is a function that takes in a function as an argument and modifies its behavior without changing its
# codebase. It does this by wrapping the function inside another function.

# Example:

def decorator_function(function):
    # define a wrapper function
    def wrapper():
        # call the function
        function()
    # return a reference of the wrapper function
    return wrapper

def say_hello():
    print("Hello!")

# "Decorating the say_hello function". This returns a reference to the wrapper function which can then be called as
# any other normal function
decorated_function = decorator_function(say_hello)
decorated_function()

# A key principle to understanding decorators is understanding that functions are first-class objects. This means
# that functions can be passed as parameters to other functions, assigned to variables, returned after a function
# call, etc.


# --------------------------------------------------------------

# 2. How do we exactly modify the behavior of a function using decorators?

def decorator_function(function):
    def wrapper(*args, **kwargs):
        print("Before Function Call")
        # the function being called here is the 'multiply' function that is defined below. it returns the product of
        # whatever argument is being passed into it. Once we get the return value, we can extend on this function
        # however we want(i.e. add it to a list, check it against a conditional, etc..)
        result = function(*args, **kwargs)
        print(result)
        print("After Function Call")
    return wrapper


def multiply(a, b):
    return a * b


decorator_result = decorator_function(multiply)
decorator_result(2, 3)

# ↑
# is similar to
# ↓

@decorated_function
def multiply(a, b):
    return a * b
