def grade_calculator():
    number_of_grades = input("How many grades do you have currently?")
    try:
        number_of_grades = int(number_of_grades)
        if number_of_grades <= 0:
            raise ValueError("You must enter at least one grade to get the average.")
    except:
        raise Exception("Invalid number of grades. Enter an integer greater than 0.")
    
    summation = 0
    for i in range(number_of_grades):
        grade_value = input("Enter a grade: ")
        try:
            grade_value = int(grade_value)
            
            if grade_value > 100 or grade_value < 0:
                raise ValueError("Grade must be between 0 and 100.")
        except ValueError:
            raise Exception("Invalid input. The value must be an integer between 0 and 100.")

        summation += grade_value

    avg = summation / number_of_grades
    print("The average is " + str(avg))

grade_calculator()


