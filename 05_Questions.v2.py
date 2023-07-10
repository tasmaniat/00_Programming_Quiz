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


# List for checking responses
emh_level = ["easy", "medium", "hard"]

end_game = "no"
while end_game == "no":
    print()

    # Ask user for choice and check if it's valid
    user_choice = choice_checker("What level would you like to play? ",
                                 emh_level,
                                 "Please choose Easy / Medium / Hard ")

    if user_choice == "xxx":
        break

    rounds_played = 0
    correct_answers = 0

    num_questions = check_rounds()

    while rounds_played < num_questions:
        print("Question: {}".format(rounds_played + 1))

        if rounds_played == num_questions:
            break


        # Generates an equation based on the chosen level
        def play_round(difficulty):
            if difficulty == "easy" or difficulty == "e":
                x = random.randint(1, 12)
                result = 4 * x
                question = f"What is x: 4x = {result}"

            elif difficulty == "medium" or difficulty == "m":
                x = random.randint(1, 12)
                num_one = random.randint(1, 12)
                result = num_one * x
                question = f"Find what x is: {num_one} * x = {result}"
            else:
                x = random.randint(1, 15)
                num_two = random.randint(1, 15)
                num_three = random.randint(1, 15)
                result = num_two * x + num_three
                question = f"Find what x is: {num_two}x + {num_three} = {result}"

            print(question)

            # Asks user for answer and to validate it.
            while True:
                response = input("Your answer: ")
                if response.isdigit():
                    user_answer = int(response)
                    break
                if response.lower() == "xxx":
                    print("Quiz ended. Thank you for playing")
                    exit()
                else:
                    # checks if user answer is valid
                    print("Please enter a valid integer.")
                    print()

            # checks if user answer is correct
            if user_answer == x:
                print("Correct!")
                print()
                return True
            else:
                print(f"Wrong! The correct answer is {x}.")
                print()
                return


        success = play_round(user_choice)
        if success:
            correct_answers += 1

        rounds_played += 1

    # Temporary total of
    print("Quiz complete!")
    print()
    print("--Total:--")
    print("  {} / {} ".format(correct_answers, num_questions))
    print("----------")
    print()

    # ask to play again.
    play_again = input("Play again? (yes/no) ")
    if play_again.lower() != "yes" and play_again.lower() != "y":
        print()
        print("Thank you for playing")
        break
