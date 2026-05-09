# Dictionaries have labelled data (keys)
# cannot have duplicate keys
# Cannot alter order of items in a dictionary

my_dict = {'A': 1, 'B': 2, 'C': 3}
print(my_dict) # Output: {'A': 1, 'B': 2, 'C': 3}

print(my_dict['A']) # Output: 1

my_dict['D'] = 4
print(my_dict) # Output: {'A': 1, 'B': 2, 'C': 3, 'D': 4}

my_dict['A'] = 5
print(my_dict) # Output: {'A': 5, 'B': 2, 'C': 3, 'D': 4} - the value of key 'A' is updated to 5

# print(my_dict['E']) # KeyError: 'E' does not exist in the dictionary

my_dict.get('E', 'Key does not exist') # Output: 'Key does not exist'

print('A' in my_dict) # Output: True
print('E' in my_dict) # Output: False

for key, value in my_dict.items():
    print(f"{key}:{value}")
