def decorator_func(func):
    def wrapper():
        print("Decorator Applied")
        return func()
    return wrapper

def apply_decorator(func):
    # Apply the decorator to the function
    decorated_func = decorator_func(func)
    return decorated_func

# function to be decorated
def example_function():
    print("Original function called")

# Applying the decorator
decorated_function = apply_decorator(example_function)

# Calling the function
decorated_function()
# Applying the decorator and calling the decorated function
decorated_function = apply_decorator(example_function)
decorated_function()
