board = [["-","-","-","-",],["-","-","-","-",],
["-","-","-","-",],["-","-","-","-",]]
import random
def make_move(board, move):
    row_pos = random.randint(0, len(board)-1)
    col_pos = random.randint(0, len(board)-1)
    for i in range(len(board)):
        if board[row_pos][col_pos] == move:
            row_pos = random.randint(0, len(board)-1)
            col_pos = random.randint(0, len(board)-1)

    board[row_pos][col_pos] = move


for j in range(10):
    make_move(board, "X")
    print(board)

def geometric_series(m:int):
    first_term = 1/2
    second_term = 1/4
    ratio = second_term / first_term
    sum = (first_term * (1 - (ratio)**m)) / (1 - ratio)
    return sum

print(geometric_series(2))

    
def table_of_approximations(p:int):
    if p < 1:
        raise Exception("Bad parameter")
    if type(p) != int:
        raise Exception("Bad parameter")
    else:        
        print("p          sum")
        print("---------------------------")
        for i in range(p):
            result = str(i+1) + "          " + str(geometric_series(i+1))
            print(result)

def even(my_list):
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            return my_list[i]

print(even([1,3,5,1,2,34,4,5,66,7,8,9,2]))

a = [[1,2,3,4,5,6,7],[6,6,4,6,8,7,4],[2,6,8,5,9,7,9]]
def sumColumn(a, col):
    sum_col = 0
    for row in range(len(a)):
        for j in range(len(a[row])):
            if j == (col-1):
                sum_col = sum_col + a[row][j]
    return sum_col


print(sumColumn([[1,2,3,4,5,6,7],[6,6,4,6,8,7,4],[2,6,8,5,9,7,9]], 7))

    
def reverse_list(a:list):
    rev_list = []
    for i in range(len(a)):
        rev_list.append(a[len(a) - i - 1])
    return rev_list

print(reverse_list([1,2,3,4,5,6,7]))
        
#Question_13
def curve(grades:list):
    best = max(grades)
    letter_grades_list = []
    for i in range(len(grades)):
        if grades[i] >= (best - 10):
            letter_grades_list.append('A')
        elif grades[i] >= (best - 20):
            letter_grades_list.append('B')
        elif grades[i] >= (best - 30):
            letter_grades_list.append('C')
        elif grades[i] >= (best - 40):
            letter_grades_list.append('D')
        else:
            letter_grades_list.append('F')
    return letter_grades_list          

print(curve([10,29,33,49,50,60,70]))

a = [1,2,3,44,55,6,667,78,4,3]
print(max(a))

def largest_num(a:list):
    largest = a[0]
    for i in range(len(a)):
        if a[i] > largest:
            largest = a[i]
    return largest
a = [1,2,3,44,55,6,67,78,4,3]
print(largest_num(a))

import random
def guessing_game(items:list):
    if len(items) < 20:
        raise Exception("At least 20 items needed.")
    else:
        
        garbage_list = ['test']

        for i in range(len(items)):
            n = random.randint(0, len(items)-1)
            option = items[n]
            for j in range(len(garbage_list)):
                if option == garbage_list[j]:
                    option = items[random.randint(0, len(items)-1)]
            print("Is it a " + str(option))
            garbage_list.append(option)
            result = input()
            if result == "yes":
                print("I win")
                break
    return ""
print(guessing_game(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']))

def clean2D(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == None or a[i][j] < 0:
                a[i][j] = 0
            elif a[i][j] > 100:
                a[i][j] = 100
            a[i][j] = round(a[i][j])
    return a
print(clean2D([[3.5, 2, 1, -6, None], [None, 12.2, -5, 1, None, None]]))
      
