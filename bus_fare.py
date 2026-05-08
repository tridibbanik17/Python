"""
Children 12 or under are free
People aged 13-17, 65+, and students pay half price
Everyone else pays full price
"""

raw_age = input("What is your age? ").strip()

# Error handling for invalid input types
if not raw_age.isnumeric():
    print("Invalid age. Age must be an integer.")
    exit()

age = int(raw_age)  # Convert the input to an integer

# Error handling for invalid age values
if (age < 0):
    print("Invalid age. Age cannot be negative.")
    exit()

if (age > 120):
    print("Invalid age. Age cannot be greater than 120.")
    exit()

if (age == 0):
    print("Invalid age. Age cannot be 0.")
    exit()

no_price   = 0
full_price = 3.50
half_price = full_price / 2

if (age <= 12):
    print(f"Your bus fare is ${no_price:.2f}")
elif (13 <= age <= 17):
    print(f"Your bus fare is ${half_price:.2f}")
elif (age >= 65):
    print(f"Your bus fare is ${half_price:.2f}")
else:
    student_or_not = input("Enter YES if you're a student: ").strip().upper()
    if (student_or_not == "YES"):
        print(f"Your bus fare is ${half_price:.2f}")
    else:
        print(f"Your bus fare is ${full_price:.2f}")


