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
