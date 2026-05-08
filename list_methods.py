letters = ['a', 'b', 'c', 'd', 'e']
print(letters)  # Output: ['a', 'b', 'c', 'd', 'e']

letters.extend(['a', 'b'])  # Extend the list by adding elements from another list
print(letters)  # Output: ['a', 'b', 'c', 'd', 'e', 'a', 'b']
####### list can contain duplicate elements

letters.append('a')  # Append a single element to the end of the list
print(letters)  # Output: ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'a']

letters.append([1, 2])  # Append a list as a single element to the end of the list
print(letters)  # Output: ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'a', [1, 2]]

letters.remove('a')  # Remove the first occurrence of 'a' from the list
print(letters)  # Output: ['b', 'c', 'd', 'e', 'a', 'b', 'a', [1, 2]] 

letters.count('a')  # Count the number of occurrences of 'a' in the list, which is 2
print(letters)  # Output: ['b', 'c', 'd', 'e', 'a', 'b', 'a', [1, 2]]

letters.index('a')  # Find the index of the first occurrence of 'a' in the list, which is 4
print(letters)  # Output: ['b', 'c', 'd', 'e', 'a', 'b', 'a', [1, 2]]

# letters.index('f')  # This will raise a ValueError because 'f' is not in the list

letters.insert(0, 'z')  # Insert 'z' at index 0 (the beginning of the list)
print(letters)  # Output: ['z', 'b', 'c', 'd', 'e', 'a', 'b', 'a', [1, 2]]

pop_return = letters.pop(0)  # Remove the element at index 0, which is 'z'
print(pop_return)  # Output: 'z'
print(letters)  # Output: ['b', 'c', 'd', 'e', 'a', 'b', 'a', [1, 2]]

print(letters,id(letters)) 
letters.reverse()  # Reverse the order of the elements in the list
print(letters, id(letters))  # Output: [[1, 2], 'a', 'b', 'a', 'e', 'd', 'c', 'b']

print(letters[::-1], id(letters[::-1]))  # Output: ['b', 'c', 'd', 'e', 'a', 'b', 'a', [1, 2]]
# letters.reverse() vs letters[::-1]
# letters.reverse() will reverse the list in place, meaning it will modify the original list and not create a new one.
# letters[::-1] will create a new list that is the reverse of the original list and will not modify the original list.

# letters.sort()  # Sort the elements of the list in ascending order
                  # However, this will raise a TypeError because the list contains both strings and a list, which cannot be compared for sorting.
letters.remove([1, 2])  # Remove the list [1, 2] from the list
print(letters)  # Output: [[1, 2], 'a', 'a', 'b', 'b', 'c', 'd', 'e']

letters.sort()  # Sort the elements of the list in ascending order
print(letters)  # Output: ['a', 'a', 'b', 'b', 'c', 'd', 'e']

letters.sort(reverse=True)  # Sort the elements of the list in descending order
print(letters)  # Output: ['e', 'd', 'c', 'b', 'b', 'a', 'a', [1, 2]]

print('a' in letters)  # Check if 'a' is in the list, which is True
print('f' in letters)  # Check if 'f' is in the list, which is False

# A Python list can contains any data type
mixed_list = [1, 'hello', 3.14, [1, 2], {'key': 'value'}, (1, 2), {1, 2}] # [int, str, float, list, dict, tuple, set]
print(mixed_list)  # Output: [1, 'hello', 3.14, [1, 2], {'key': 'value'}, (1, 2), {1, 2}]

# Summary of properties of lists:
# 1. Lists are ordered collections of items, meaning that the order of the items is preserved.
# 2. Lists are mutable, meaning that you can change the contents of a list after
# 3. Lists can contain duplicate elements, meaning that the same value can appear multiple times in a list.
# 4. Lists can contain any data type, including other lists, dictionaries, tuples, sets, and even functions or classes.
# 5. List items can be accessed using indexing and slicing, which allows you to retrieve specific elements or subsets of the list.