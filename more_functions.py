# Optional parameters
def add(a, b, precision=2): # a and b are required parameters, precision is an optional parameter with a default value of 2
    # Docstrings
    """Returns the sum of a and b rounded to the specified number of decimal places (precision)."""
    a = float(a) # Convert a to a float
    b = float(b) # Convert b to a float
    return round(a + b, precision)

print(add(1.2345, 2.3456)) # Output: 3.58
print(add(1.2345, 2.3456, None)) # Output: 4
print(add(1.2345, 2.3456, 1)) # Output: 3.6

# Keyword arguments
print(add(a=2, b=3)) # Output: 5.00 (keyword arguments allow us to specify the values of parameters by name, making the code more readable)
print(add(b=3, a=2)) # Output: 5.00 (the order of keyword arguments does not matter)
print(add(2,3)) # Output: 5.00 (positional arguments, where the order of the arguments matters)

help(add) # Output: Help on function add in module __main__: add(a, b, precision=2) """docstrings"""

# Nested functions
def add(a, b, precision=2):
    def convert_to_float(x):
        if isinstance(x, str):
            if x.isnumeric():
                return int(x)
        return float(x)
    a = convert_to_float(a)
    b = convert_to_float(b)
    return round(a + b, precision)

print(add('2','3'))
print(add(1.2345, 2.3456))

# *args and **kwargs
def add(a, b):
    a = float(a)
    b = float(b)
    return round(a + b, 2)

print(add(1.2345, 2.3456))  # Output: 3.58
print(add('1.2345', '2.3456'))  # Output: 3.58

args = [-1, -2]
kwargs = {'a': '9', 'b': '0.9'}
# *args expands list into positional arguments
print(add(*args))  # equivalent to add(-1, -2) 
# **kwargs expands dictionary into keyword arguments
print(add(**kwargs))  # equivalent to add(a='9', b='0.9')