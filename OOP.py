'''
import math
class Circle:
    def __init__(self, color, radius):
        self.color = color
        self.radius = radius
        self.x = 0
        self.y = 0

    def get_area(self):
        return "The area of the circle is ", math.pi * self.radius ** 2

    def set_radius(self, radius):
        self.radius = radius
        return self.radius
    def __str__(self):
        return "This is a Circle with radius "+ str(self.radius)+ " and color "+ str(self.color) + " @ x = " + str(self.x) + " and y = " + str(self.y)

c = Circle("blue", 10)
#c.radius = 10
print(c.radius)
print(c.color)
print(c.x)
print(c.y)
print(c)
c.color = "red"
print(c)
'''
import random
class Poll:
    """ This class can be used to instantiate polls. """

    def __init__(self, question:str, options:list):
        """ Initializes the poll with a given question and a list of options"""
        self.question = question
        self.options = options
        self.start_num = 10
        self.votes = [self.start_num]*len(options)
        self.poll_open = False
        

    def open(self):
        """ Opens the poll """
        self.poll_open = True

    def close(self):
        """ Closes the poll """
        self.poll_open = False

    def vote(self, option):
        """ Records a vote if the poll is open.
            Otherwise throws an exception. Assumes poll
            options are numbered from 1. """
        #if not self.poll_open:
            #raise Exception("Poll is closed")
        self.votes[option-1] = self.votes[option-1] + 1

    def get_votes(self):
        """ Returns the number of votes for each option """
        return self.votes

    def get_num_exceptions(self):
        """counts the number of attempts while the poll was closed"""
        count = 0
        if self.poll_open == False:
            for j in range(len(self.options)):
                count+= self.votes[j]
                
        return count
       
            
            

    def get_leader(self):
        """ Identifies and returns the poll option with the greatest number
            of votes. If there is a tie, returns the lowest-numbered option
            with the greatest number of votes."""
        leader = 0
        for i in range(1,len(self.votes)):
            if self.votes[i] > self.votes[leader]:
                leader = i
        return self.options[leader]

    def __str__(self):
        for i in range(1000):
            self.vote(random.randint(1, 4))
            result = "Option 1 got " + str(self.get_votes()[0]) + " votes.\n"
            result += "Option 2 got " + str(self.get_votes()[1]) + " votes.\n"
            result += "Option 3 got " + str(self.get_votes()[2]) + " votes.\n"
            result += "Option 4 got " + str(self.get_votes()[3]) + " votes."
            result += "\nThe number of votes casted while poll was closed "+str(self.get_num_exceptions())

        return result

                
fruit_poll = Poll("Favorite Fruit?",["Strawberry", "Mango", "Bananas", "Grapes"])
print(fruit_poll)        
            
        #return result
        #return "The current leader is: "+ self.get_leader()



def even(list_num):
    for i in list_num:
        if i % 2 == 0:
            break
    return i
print(even([1,2,4,5,6,7,8]))

import random
def guessing_game(word_list, word_num):
    #word_list[random.randint(0,word_num-1)]
    if word_num < 20:
        raise Exception("The list should have at least 20 different items.")
    if word_num >= 20:
        print("Hi, let’s play a guessing game. Think of an animal and press a\n" + 
        "key when you are ready.\n")
        for i in range(word_num):
            print("Is it a " + word_list[random.randint(0, word_num-1)] + " ?")
            user_input = input()            
            if user_input == "yes":
                print("I win!!!")
                return ""

    return ""

guessing_game(["a","b","c","d","e", "f","g","h","i","j","k","l","m", "n","o", "p", "q", "r", "s", "t"], 20)

# Test Code
'''
fruit_poll = Poll("Favorite Fruit?",["Strawberry", "Mango", "Bananas", "Grapes"])
print(fruit_poll)
fruit_poll.open()
for i in range(1000):
    fruit_poll.vote(random.randint(1, 4))
fruit_poll.close()
print(fruit_poll.get_leader())
'''
'''
()
            if a == 1:
                option_1_list.append("1")
                print(option_1_list)
            if a == 2:
                option_2_list.append("2")
            if a == 3:
                option_3_list.append("2")
            if a == 4:
                option_4_list.append("2")
            result = "Option 1 got: " + str(len(option_1_list)) + " votes." + "\n Option 2 got: " + str(len(option_2_list)) + " votes." + "\n Option 3 got: " + str(len(option_3_list)) + " votes." + "\n Option 4 got: " + str(len(option_4_list)) + " votes."
            
        
'''


                
                
