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


# Main Routine
while True:
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
    print("Quiz completed. Your score is {}/{}".format(score, rounds_played if num_questions == float(
        'inf') else num_questions))
    print()

    play_again = input("Play again? (yes/no) ")
    if play_again.lower() != "yes" and play_again.lower() != "y":
        break
