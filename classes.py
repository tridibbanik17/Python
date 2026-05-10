# instatiate a class: obj = MyClass()
# call a method: obj.method()
# access a class attribute: MyClass.attr
# access an instance attribute: obj.attr
# When a class is instatiated, the __init__ method is called automatically to initialize the instance attributes. 
# When return f"{self}" is used in a method, it calls the __str__ method to get the string representation of the instance.


class MyClass:

    # Class attributes
    attr1 = 'A'
    attr2 = 'B'

    # Instance attributes
    def __init__(self, attr1='Hello'): # attr1 is optional, default value is 'Hello'
        print(f"{self} is initialized")
        self.attr1 = attr1
        self.attr2 = 'B'

    def a_method(self):
        print(f"Called a_method of {self}")

    def __str__(self):
        return f'Instance ({self.attr1}, {self.attr2})'


class Horse:

    def __init__(self, age, colour):
        self.age = age
        self.colour = colour

    def trot(self):
        print(f"Called trot of {self}")

    def __str__(self):
        return f"{self.colour.capitalize()} horse, {self.age} years old"


# --- Class objects ---
print("MyClass as a class object:    ", MyClass)
print("Horse as a class object:      ", Horse)
print("Built-in str as a class object:", str)
print("Type of MyClass:               ", type(MyClass))

# --- MyClass instances ---
obj = MyClass()
print("MyClass instance (obj):        ", obj)

# --- Horse instances ---
obj2 = Horse(5, 'black')
print("Horse instance (obj2):         ", obj2)

obj = obj2                              # obj now points to the same Horse instance as obj2
print("obj after reassignment:        ", obj)
print("obj2 unchanged:                ", obj2)
print("Type of obj after reassignment:", type(obj))

# --- Method calls: unbound vs bound ---
my_class_instance = MyClass()
print("Unbound method call:")
MyClass.a_method(my_class_instance)     # explicitly passing the instance
print("Bound method call:")
my_class_instance.a_method()           # instance passed automatically as self

horse_instance = Horse(3, 'chestnut')
print("Unbound method call:")
Horse.trot(horse_instance)             # explicitly passing the instance
print("Bound method call:")
horse_instance.trot()                  # instance passed automatically as self

# --- Attribute access ---
print("my_class_instance.attr1 (instance attribute):", my_class_instance.attr1)
print("horse_instance.age (instance attribute):     ", horse_instance.age)

