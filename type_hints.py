# functions
def add(n1: int, n2: int) -> int:
    return n1 + n2

# variables
total: int = add(1, 2)  
print("Total:", total)  # prints: Total: 3

# containers
totals: list[int] = [10, 20, 30]

# multiple options
def add_multiple_options(n1: int | float, n2: int | float) -> int | float:
    return n1 + n2

total_with_multiple_options: int | float = add_multiple_options(1, 2.5)
print("Total with multiple options:", total)  # prints: Total with multiple options: 3.5