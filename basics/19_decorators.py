def print_call(function):
    def print_function():
        print(f'The function {function.__name__} was executed')
        return function
    return print_function

@print_call
def example_function():
    pass

@print_call
def example_function2():
    pass

@print_call
def example_function3():
    pass

example_function()
example_function2()
example_function3()

def call_counter(function):
    def counter_function():
        counter_function.call_count += 1
        print(f'The function {function.__name__} was called {counter_function.call_count} times')
        return function
    counter_function.call_count = 0 
    return counter_function

@call_counter
def example1():
    pass

@call_counter
def example2():
    pass

@call_counter
def example3():
    pass
