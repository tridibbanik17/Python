with open('input.txt') as file:
    print(file)
    print(file.read())
    file.close()

with open('input.txt') as file:
    sum = 0
    # read the file line by line
    for line in file.readlines():
        sum = sum + float(line.strip())
print(sum)