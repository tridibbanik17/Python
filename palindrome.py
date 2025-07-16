def palindrome(x):
    count = 0
    if len(str(x)) % 2 == 0: #if the number is an even number.
        for i in range(int(len(str(x)) / 2)): 
            if str(x)[i] == str(x)[len(str(x)) - i - 1] :
                count += 1
             
        if count == len(str(x)) // 2:
            return True
        else:
            return False


    count = 0
    if len(str(x)) % 2 != 0: #if the number is an odd number.
        for i in range(len(str(x)) // 2): 
            if str(x)[i] == str(x)[len(str(x)) - i - 1] :
                count += 1
            
        if count == len(str(x)) // 2:
            return True
        else:
            return False
