# Print how many vowels an input word contains.

word = input("Type a word: ").lower()
counter = 0
for letter in word: 
    if letter in "aeiou":
        counter += 1
print(f"There are {counter} vowels in {word}.")