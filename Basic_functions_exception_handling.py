'''
#Test Cases
def conversion(amount):
    try:
        if amount < 0:
            raise ValueError("The amount cannot be negative.")
        a = amount * 80
        return a
    except ValueError:
        print("Enter an integer.")
        return 0.0
    except TypeError:
        print("Enter an integer.")
        return 0.0
    except:
        print("An occur has occurred.")
        return 0.0
def test_exercise_1():
    inputs = [1, "", -1]
    expected = [80.0, 0.0, 0.0]

    for i in range(len(inputs)):
        print(i+1)
        actual = conversion(inputs[i])
        expect = expected[i]
        print("Expected: ", expected)
        print("Actual: ", actual)

        if actual == expect:
            print("PASS.")
        else:
            print("FAIL.")
    return ""
    
print(test_exercise_1())

'''
'''
def conversion(amount):
    try:
        rate = 80.0
        amount_in_bdt = int(amount) * rate
    except ValueError:
        #print("Enter an integer.")
        return 0.0
    if amount < 0:
        #raise Exception("Negative amount received.")
        return "Negative amount received."
    
    return amount_in_bdt

def test_exercise_1():
    case_type = [" (path)", " (special)", " (boundary)"]
    inputs = [1.0, "hello", -1.0]
    expected = [80.0, 0.0, "Negative amount received."]
    actual = []
    for i in range(3):
        actual.append(conversion(inputs[i]))
        print("Test case#" + str(i+1) + case_type[i])
        print("Input: ", inputs[i])
        print("Expected Output: ", expected[i])
        print("Actual Output: ", actual[i])
        if actual[i] == expected[i]:
            print("Result: PASS")
            print()
        else:
            print("Result: Fail")
            print()
    return
'''
import math        
def quadratic_roots(a, b, c):
    try:
        if int(b)**2 - 4*int(a)*int(c) < 0:
            #raise Exception("No roots")
            return False
    
        x_1 = (-int(b) + math.sqrt(int(b)**2 - 4*int(a)*int(c))) / (2*int(a))
        x_2 = (-int(b) - math.sqrt(int(b)**2 - 4*int(a)*int(c))) / (2*int(a))

        if x_1 == x_2:
            return [x_1]
        else:
            return [x_1, x_2]
    except ValueError:
        print("Enter an integer.")
        return False
    except ZeroDivisionError:
        print("Can't divide by zero.")
        return False

'''Name:Tridib Banik
MacID: banikt
st#: 400514461'''

def test_exercise_2():
    case_type = [" (boundary)", " (boundary)", " (path)", " (special)"]
    inputs = [[1, 2, 1], [1,1,1], [1,-5,6], [1,"",2]]
    expected = [[-1], False, [3,2], False]
    actual = []
    for i in range(4):
        print("Test Case#" + str(i+1) + case_type[i])
        print("Input: ", inputs[i])
        print("Expected: ", expected[i])
        actual.append(quadratic_roots(inputs[i][0], inputs[i][1], inputs[i][2]))
        print("Actual: ", actual[i])
        if actual[i] == expected[i]:
            print("Result: PASS")
            print()
        else:
            print("Result: FAIL")
            print()
    return ""

test_exercise_2()


'''

def conversion(amount):
    #Try and except block.
    try:
        if amount < 0:
            raise ValueError("Negative Amount Received.")
        #1 CAD = 80.0 BDT
        amount_bdt = float(amount) * 80.0
        return amount_bdt
    #if type error, the function returns 0.0
    except TypeError:
        print("Please enter an integer.")
        return 0.0
    except ValueError:
        print("Negative Amount Received.")
        return 0.0

print(conversion(1))
print(conversion("help"))
print(conversion(-1))


#Test cases
def test_exercise1():
    #A list of inputs
    inputs = [1, "help", -1]
    #A list of expected outputs of the inputs respectively.
    expected = [80.0, 0.0, 0.0]
    #initializing an empty list.
    actual = []
    #since there are three cases, there are three inputs and so three iterations.
    for i in range(3):
        print("Test case: ", i+1)
        print("input: ", inputs[i])
        print("expected output: ", expected[i])
        #For every iteration, expected actual output after running the conversion function will be addded to the empty list.
        actual.append(conversion(inputs[i]))
        print("actual output: ", actual[i])
        #if actual output matches the expected output, it is a pass.
        if actual[i] == expected[i]:
            print("PASS")
            print()
        else:
            print("FAIL")
            print()
#Call the function.
test_exercise1()
        
        
'''
    
        
