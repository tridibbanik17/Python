print(f"'i' in 'team' is {'i' in 'team'}")                     # False
print(f"'i' in 'win' is {'i' in 'win'}")                       # True

print(f"isinstance(10, int) is {isinstance(10, int)}")         # True
print(f"isinstance(10.0, int) is {isinstance(10.0, int)}")     # False

print(f"'HELLO'.isupper() is {'HELLO'.isupper()}")             # True
print(f"'pAssW0rD1'.isalnum() is {'pAssW0rD1'.isalnum()}")     # True
print(f"'pAssW0rD1'.isalpha() is {'pAssW0rD1'.isalpha()}")     # False

print(f"'3.14'.isnumeric() is {'3.14'.isnumeric()}")           # False
print(f"'1400'.isnumeric() is {'1400'.isnumeric()}")           # True

print(f"True is True is {True is True}")                       # True
print(f"True is False is {True is False}")                     # False

print(f"True == True is {True == True}")                       # True
print(f"True == False is {True == False}")                     # False

print(f"True != True is {True != True}")                       # False
print(f"True != False is {True != False}")                     # True

print(f"1 is 1 is {1 is 1}")                                   # True
print(f"1 is 1.0 is {1 is 1.0}")                               # False
print(f"1 is not 1.0 is {1 is not 1.0}")                       # True
print(f"1 == 1.0 is {1 == 1.0}")                               # True
print(f"1 != 1.0 is {1 != 1.0}")                               # False

print(f"'a b c' == 'a b c' is {'a b c' == 'a b c'}")           # True
print(f"'a b c' is 'a b c' is {'a b c' is 'a b c'}")           # True (string interning)

print(f"'time' > 'money' is {'time' > 'money'}")               # True (because 't' has a higher ASCII value than 'm')
print(f"'time' < 'money' is {'time' < 'money'}")               # False

print(f"'time' == 'turn' is {'time' == 'turn'}")               # False
print(f"'time' >= 'turn' is {'time' >= 'turn'}")               # False
print(f"'time' <= 'turn' is {'time' <= 'turn'}")               # True

print(f"Boolean of empty string is {bool('')}" )               # False (empty string is falsy) 
print(f"Boolean of non-empty string is {bool(' ')}")           # True (non-empty string is truthy)

print(f"Boolean of 0 is {bool(0)}")                           # False (0 is falsy)
print(f"Boolean of non-zero number is {bool(0.1)}")           # True (non-zero number is truthy)

print(f"Boolean of None is {bool(None)}")                     # False (None is falsy)
print(f"Boolean of empty list is {bool([])}")                 # False (empty list is falsy)
print(f"Boolean of empty dict is {bool({})}")                 # False (empty dictionary is falsy)

print(f"Boolean of empty tuple is {bool(())}")                # False (empty tuple is falsy)
print(f"Boolean of tuple with one element is {bool((1,))}")   # True (tuple with one element is truthy)

print(f"Boolean of empty set is {bool(set())}")               # False (empty set is falsy)
print(f"Boolean of set with one element is {bool({1})}")      # True (set with one element is truthy)

print(f"Boolean of empty range is {bool(range(0))}")          # False (empty range is falsy)
print(f"Boolean of range with 1 element is {bool(range(1))}") # True (range with one element is truthy)

print(f"0 == False is {0 == False}")                          # True (0 is equal to False)
print(f"0 is False is {0 is False}")                          # False (0 and False are not the same object)

print(f"0 == None is {0 == None}")                           # False (0 is not equal to None)
print(f"0 is None is {0 is None}")                           # False (0 and None are not the same object)