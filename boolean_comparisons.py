print(f'True and True is {True and True}')           # Always True
print(f'True and False is {True and False}')         # Always False
print(f'False and False is {False and False}')       # Always False
print()
print(f'True or True is {True or True}')             # Always True
print(f'True or False is {True or False}')           # Always True
print(f'False or False is {False or False}')         # Always False
print()
print(f'not True is {not True}')                     # Always False
print(f'not False is {not False}')                   # Always True
print()

print(f'True and not True is {True and not True}')  # Always False
print(f'True or not True is {True or not True}')    # Always True

rain = True
snow = False
print(rain and snow) # False
print(not rain and not snow) # False
print((rain and snow) or (not rain and not snow)) # False (Use brackets to group conditions)
