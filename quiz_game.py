# Create a list of answers (e.g., countries that start with 'V')
# The user tries to get all of the answers
# If they give up and quit, print out all of the ones that were missed

def play():
    answer_list = ["Vatican City", "Vanuatu", "Venezuela", "Vietnam"]
    num_of_answers = len(answer_list)
    user_answer_list = []
    missed_answers = []
    print("""
          Game rules:
          - You have to guess the countries that start with 'V'.
          - You can guess in any order.
          - You can only guess one country at a time.
          - You can quit at any time by typing 'Quit'.
          """)
    while len(user_answer_list) != len(answer_list):
        if num_of_answers == 1:
            suffix = ''
        else:
            suffix = 's'
        print(f"{num_of_answers} correct answer{suffix} remaining.")
        user_answer = input("Enter the country: ").strip().title()
        if user_answer in user_answer_list:
            print("Already guessed. Try again.")
        elif user_answer in answer_list:
            user_answer_list.append(user_answer)
            print("Correct!")
            num_of_answers = num_of_answers - 1
        elif user_answer == 'Quit':
            for answer in answer_list:
                if answer not in user_answer_list:
                    missed_answers.append(answer)
            print(get_missed_answers(missed_answers))
            break
        else:
            print("Incorrect. Try again.")

def get_missed_answers(missed_answers):
    if len(missed_answers) == 0:
        return "Congratulations! You got all the answers!"
    else: 
        suffix = '' if len(missed_answers) == 1 else 's'
        return f"You missed the following {len(missed_answers)} answer{suffix}: {', '.join(missed_answers)}"

if __name__ == "__main__":
    play()