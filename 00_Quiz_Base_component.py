# check user answers yes / no to a question
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("please answer yes / no")
            print()


# Prints the quiz's instructions, returns ""
def instructions():
    print()
    print("------- WELCOME TO THE ALGEBRA QUIZ -------")
    print()
    print(" - pick a level < easy / medium / hard >\n"
          " - choose how many questions u want\n")

    print(" You will be shown an equation to solve")
    print()
    print("To answer the questions correctly your goal\n"
          "is to find out what the variable 'x' is. ")
    print()
    print("Example: 2x - 1 = 5   |   Example: x + 5 = 9\n"
          "          x = 3       |            x = 4")
    print()
    return ""


# Checks user enter a valid choice based on a list
# it accepts either the first letter of the full word
# and has a custom error message. (returns the full word)
def level_choice(question, valid_list, error):
    valid = False
    while not valid:

        # ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response == item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if the item not in list
        print(error)
        print()


# checks users enter an integer that is more than zero
# or allows <enter> for infinite mode
def check_rounds():
    while True:
        print()
        user_input = input("How many questions? ")

        # Return if user enters " " for infinity mode
        if user_input == "":
            return float('inf')

        # Exit the program if user inputs 'xxx'
        if user_input.lower() == "xxx":
            exit()

        round_error = "Please type either <enter> or an " \
                      "integer that is more than 0"

        try:
            num_questions = int(user_input)

            # checks for valid input if num less 1
            if num_questions < 1:
                print(round_error)
            else:
                # Return the valid num of questions
                return num_questions

        # If a non-integer is entered,
        # ask for valid input.
        except ValueError:
            print(round_error)


# Main routine goes here


# Ask the user if they have played before
# Display instructions if they have not
print()
played_before = yes_no("Have you played this game before? ")

if played_before == "no":
    instructions()
    input("Press enter to continue")

# List for checking responses
emh_level = ["easy", "medium", "hard"]

# Ask user for choice and check it's valid
print()
user_choice = level_choice("What level would you like to play? ",
                           emh_level,
                           "Please choose Easy / Medium / Hard "
                           "(or xxx to quit)")

# Print out choice
if user_choice != "xxx":
    print("You chose {} Level".format(user_choice))

rounds_played = 0
score = 0

end_game = "no"
while end_game == "no":

    rounds_played = 0
    score = 0

    num_questions = check_rounds()

    while True:
        print()
        print("Question: {}".format(rounds_played + 1))
        response = input("Enter your answer (or 'xxx' to quit):\n")

        if response.lower() == "xxx":
            exit()

        # Check the answer and update the score if needed
        # To Add your logic here to check the answer
        score += 1
        rounds_played += 1

        if rounds_played == num_questions:
            break

    print()
    print("Quiz completed. ")
    print()

    play_again = input("Play again? (yes/no) ")
    if play_again.lower() != "yes" and play_again.lower() != "y":
        break
