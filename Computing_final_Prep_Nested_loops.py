'''
#Lecture_Exercise
def best_average(grades):
    
    avg_list = []
    for row in range(len(grades)):
        col_sum = [0]*len(grades)
        for col in range(len(grades[row])):
            col_sum[row] = int(col_sum[row]) + grades[row][col]
        avg = int(col_sum[row])/len(grades[row])
        avg_list.append(avg)
    highest_avg = avg_list[0]
    for i in range(len(grades)-1):
        if avg_list[i+1] > highest_avg:
            highest_avg = avg_list[i+1]
        
                    
    return highest_avg

print(best_average([[1,2,3,4,5,6,7],[6,6,4,6,8,7,4],[2,6,8,5,9,7,9]]))



#Question_13
def curve(grades):
    best = grades[0]
    for i in range(len(grades)):
        if grades[i] > best:
            best = grades[i+1]
    new_list = []
    for i in range(len(grades)):
        if grades[i] >= (best - 10):
            new_list.append([grades[i], "A"])
        elif grades[i] >= (best - 20):
            new_list.append([grades[i], "B"])
        elif grades[i] >= (best - 30):
            new_list.append([grades[i], "C"])
        elif grades[i] >= (best - 40):
            new_list.append([grades[i], "D"])
        else:
            new_list.append([grades[i], "F"])
    return new_list

print(curve([10,29,33,49,50,60,70]))

def reverse_list(my_list):
    rev_list = []
    for i in range(len(my_list)):
        rev_list.append(my_list[len(my_list) - (i+1)])
    return rev_list

print(reverse_list([1,2,3,4,5,6,7]))
        
a = [[1,2,3,4,5,6,7],[6,6,4,6,8,7,4],[2,6,8,5,9,7,9]]
def sumColumn(a, col):
    summation = []
    sum_col = 0
    for row in range(len(a)):
        for j in range(len(a[row])):
            if j == (col-1):
                sum_col = sum_col + a[row][j]
    return sum_col


print(sumColumn([[1,2,3,4,5,6,7],[6,6,4,6,8,7,4],[2,6,8,5,9,7,9]], 1))
            
        
class TV:
    def __init__(self, power:bool, channel:int, poss_input:str, volume:int):
        self.power = power
        self.channel = channel
        self.poss_input = poss_input
        self.volume = volume

    #Accessor methods.
    def get_power(self):
        return self.power
    def get_channel(self):
        return self.channel
    def get_poss_input(self):
        return self.poss_input
    def get_volume(self):
        return self.volume

    #Mutator methods.
    def set_power(self, power):
        self.power = power
        if self.power == True:
            return "TV is ON"
        else:
            return "TV is OFF."
    def set_poss_input(self, poss_input):
        self.poss_input = poss_input
        if self.power == False:
            raise Exception("TV is OFF. Turn on first to change input source.")
        else:
            if self.poss_input == "VGA":
                self.poss_input = "VGA"
            elif self.poss_input == "HDMI":
                self.poss_input = "HDMI"
            elif self.poss_input == "Cable":
                self.poss_input = "Cable"
        return self.poss_input
    def set_volume(self, volume):
        self.volume = volume
        if self.power == False:
            raise Exception("TV is OFF. Turn on first to change volume.")
        elif self.power == True:
            if self.volume < 0:
                self.volume = 0
                mute = " (muted) "
            elif self.volume > 100:
                self.volume = 100
                mute = " (not muted) "
        return str(self.volume) + mute
    def set_channel(self, channel):
        self.channel = channel
        if self.power == False:
            raise Exception("TV is OFF. Turn on first to change input source.")
        else:
            if self.poss_input != "Cable":
                return ""
            elif self.poss_input == "Cable":
                if self.channel < 1:
                    self.channel = 1
                elif self.channel > 1000:
                    self.channel = 1000
        return " channel " + str(self.channel)
    def __str__(self):
        result = str(self.set_power(self.power)) + ", Volume " + str(self.set_volume(self.volume)) + "showing " + str(self.set_poss_input(self.poss_input)) + str(self.set_channel(self.channel)) + "."
        return result

tv1 = TV(True, 99, "Cable", -9)
tv2 = TV(False, 9999999999, "Cable", 100900)
tv3 = TV(True, 9999999999, "VGA", 100900)
print(tv1)
print(tv3)
print(tv2)
'''
#Question7
def pi(i):
    sum_pi = 0 #initialize variable.
    for n in range(1, i+1):
        approx_pi = 4 * ((-1)**(n+1) / (2*n - 1))
        sum_pi = sum_pi + approx_pi
    return sum_pi

print(pi(3000000))


#Question17
import random
def make_move(board, move):
    row_pos = random.randint(0, len(board) - 1)
    col_pos = random.randint(0, len(board) - 1)
    for i in range(len(board)):
        if board[row_pos][col_pos] == move:
            row_pos = random.randint(0, len(board) - 1)
            col_pos = random.randint(0, len(board) - 1)
    board[row_pos][col_pos] = move
board = [["-","-","-","-",],["-","-","-","-",],
["-","-","-","-",],["-","-","-","-",]]
for i in range(10):
    make_move(board, "X")
    print(board)


def conversion(amount):
    try:
        if amount < 0:
            raise ValueError("Negative Amount Received")
        rate = 80.0
        amount_bdt = amount * rate
        return amount_bdt
    except TypeError:
        print("Enter an integer.")
        return 0.0
    except ValueError:
        print("Negative Amount Received")
        return 0.0

print(conversion(""))


def test_exercise_1():
    inputs = [1, -1, "help"]
    expected = [80.0, 0.0, 0.0]
    for i in range(3):
        print("Test case " + str(i+1))
        print("Input: ", inputs[i])
        print("Expected Output: ", expected[i])
        actual = conversion(inputs[i])
        print("Actual Output: ", actual)
        if actual == expected[i]:
            print("PASS")
            print()
        else:
            print("FAIL")
            print()

test_exercise_1()

    
