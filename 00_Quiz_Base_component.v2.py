import random


# Checks if the user enters a valid choice based on a list
# It accepts either the first letter of the full word
# and has a custom error message (returns the full word)
def choice_checker(question, valid_list, error):
    valid = False
    while not valid:
        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()
        # Iterate through list and if response == item
        # in the list (or the first letter of an item), the
        # full item name is returned
        for item in valid_list:
            if response == item[0] or response == item:
                return item
        # Output error if the item is not in the list
        print(error)
        print()


# Checks if the user enters an integer that is more than zero
# or allows <enter> for infinite mode
def check_rounds():
    while True:
        print()
        user_input = input("How many questions? ")
        print()

        # Return if the user enters " " for infinity mode
        if user_input == "":
            return float('inf')

        # Exit the program if the user inputs 'xxx'
        if user_input.lower() == "xxx":
            exit()

        round_error = "Please type either <enter> or an " \
                      "integer that is more than 0"

        try:
            num_questions = int(user_input)

            # Checks for valid input if num is less than 1
            if num_questions < 1:
                print(round_error)
            else:
                # Return the valid num of questions
                return num_questions

        # If a non-integer is entered,
        # ask for valid input.
        except ValueError:
            print(round_error)


# Check user answers yes / no to a question
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please answer yes / no")
            print()


# Prints the quiz's instructions, returns ""
def instructions():
    print()
    print("------- WELCOME TO THE ALGEBRA QUIZ -------")
    print()
    print(" - Pick a level <easy / medium / hard>\n"
          " - Choose how many questions you want\n")
    print("You will be shown an equation to solve")
    print()
    print("To answer the questions correctly, your goal\n"
          "is to find out what the variable 'x' is. ")
    print()
    print("Example: 2x - 1 = 5   |   Example: x + 5 = 9\n"
          "          x = 3       |            x = 4")
    print()
    return ""


# Game Statistics
best_score = float('inf')
worst_score = float('-inf')
total_score = 0


# Ask the user if they have played before
# Display instructions if they have not
print()
played_before = yes_no("Have you played this quiz before? ")

if played_before == "no":
    instructions()
    input("Press enter to continue")

game_summary = []

# List for checking responses
emh_level = ["easy", "medium", "hard", "xxx"]

# Ask user for choice and check if it's valid
print()
user_choice = choice_checker("What level would you "
                             "like to play? ", emh_level, "Please choose "
                                                          "Easy / Medium / Hard ("
                                                          "or xxx to quit)")

# Check if the user wants to quit the quiz
if user_choice == "xxx":
    print()
    print("Quiz ended. Thank you for playing!")
    exit()

# Prints out choice of level
print("You chose {} Level".format(user_choice))


end_game = "no"
while end_game == "no":
    rounds_played = 0
    rounds_correct = 0
    rounds_incorrect = 0
    score = 0

    num_questions = check_rounds()

    while rounds_played < num_questions:
        rounds_played += 1
        print("Question: {}".format(rounds_played))


        def play_round(difficulty):

            # Generates an equation based on the chosen level

            if difficulty == "easy" or difficulty == "e":
                x = random.randint(1, 12)
                quiz = 4 * x
                question = f"What is x: 4x = {quiz}"
            elif difficulty == "medium" or difficulty == "m":
                x = random.randint(1, 12)
                num_one = random.randint(1, 12)
                quiz = num_one * x
                question = f"Find what x is: {num_one} * x = {quiz}"
            else:
                x = random.randint(1, 12)
                num_two = random.randint(1, 12)
                num_three = random.randint(1, 12)
                quiz = num_two * x + num_three
                question = f"Find what x is: {num_two}x + {num_three} = {quiz}"

            print(question)

            # Asks user for answer and to validate it.
            while True:
                user_answer = input("Your answer: ")

                if user_answer.lower() == "xxx":
                    print()
                    print("Quiz ended. Thank you for playing!")
                    exit()

                try:
                    user_answer = int(user_answer)
                    if user_answer > 0:
                        break
                    else:
                        print("Please enter a number greater than 0.")
                except ValueError:
                    print()
                    print("Please enter an integer.(or xxx to quit)")

            # checks if hte user's answer is correct
            if user_answer == x:
                print("Correct!")
                print()
                return "Correct  ", 1
            else:
                print(f"Wrong! The correct answer is {x}.")
                print()
                return "Incorrect", 0


        success = play_round(user_choice)
        result, question_score = success
        game_summary.append((rounds_played, result, question_score))
        score += question_score

    total_score += score
    rounds_correct += score
    rounds_incorrect += num_questions - score
    result = ""

    if score < best_score:
        best_score = score

    if score > worst_score:
        worst_score = score

    print()
    print("Quiz completed.")
    print()

    # ***** Calculate quiz statistics *****
    average_score = total_score / rounds_played if rounds_played != 0 else 0
    percent_correct = rounds_correct / (rounds_correct + rounds_incorrect) * 100
    percent_incorrect = rounds_incorrect / (rounds_correct + rounds_incorrect) * 100

    # End of quiz statements

    print("----------------------------")
    print("Correct: {}\t|\tIncorrect: {} ".format(rounds_correct, rounds_incorrect))
    print("----------------------------")
    print()

    # Ask the user if they want to see the game statistics
    show_statistics = yes_no("Do you want to see the game Statistics?")
    print()
    if show_statistics == "yes":
        # Displays the quiz scores
        # Shows the results of the questions in the game and
        # what their score is
        print()
        print("*********** Quiz Scores **********")
        print(" Question | Result\t\t| Score")
        print()
        for i, item in enumerate(game_summary, 1):
            question_number, result, question_score = item
            print(" {}\t\t  | {}\t| {}".format(question_number, result, question_score))

        # Show game statistics
        # Displays the best, worst, and average scores of the game
        print("\n******* Summary Statistics *******")
        print("Best Score: {}\nWorst Score: {}\nAverage Score: {:.2f}"
              .format(best_score, worst_score, average_score))
        print()

    play_again = input("Play again? (yes/no) ")
    if play_again.lower() == "no" or play_again.lower() == "n":
        end_game = "yes"
        print()
        print("Thank you for playing!")
    else:
        # List for checking responses
        emh_level = ["easy", "medium", "hard", "xxx"]

        # Ask user for choice and check if it's valid
        print()
        user_choice = choice_checker("What level would you "
                                     "like to play? ", emh_level, "Please choose "
                                                                  "Easy / Medium / Hard ("
                                                                  "or xxx to quit)")

        # Check if the user wants to quit the quiz
        if user_choice == "xxx":
            print()
            print("Quiz ended. Thank you for playing!")
            exit()

        # Prints out choice of level
        print("You chose {} Level".format(user_choice))

        game_summary = []
