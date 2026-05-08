list1 = ['a', 'b', 'c']
print(list1, id(list1)) # Output: ['a', 'b', 'c'] <memory_address>

list1[0] = 'A'  # Modifying the first element of the list
print(list1, id(list1)) # Output: ['A', 'b', 'c'] <same_memory_address>

list1.append('d')  # Adding an element to the end of the list
print(list1, id(list1)) # Output: ['A', 'b', 'c', 'd'] <same_memory_address>

list2 = list1  # This creates a reference to the same list, not a copy
print(list1, id(list1)) # Output: ['A', 'b', 'c'] <memory_address>
print(list2, id(list2)) # Output: ['A', 'b', 'c'] <same_memory_address>

list3 = list(list1)  # This creates a new list that is a copy of the original list
print(list1, id(list1)) # Output: ['A', 'b', 'c'] <memory_address>
print(list2, id(list2)) # Output: ['A', 'b', 'c'] <same_memory_address>
print(list3, id(list3)) # Output: ['A', 'b', 'c'] <different_memory_address> 
