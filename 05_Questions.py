import random

rounds = 0
rounds_played = 0
game_summary = []


# checks user enters an integer between a low and high number
def int_check(question, low=None, high=None, exit_code=None):
    if low is None and high is None:
        error = "Please enter an integer"
        situation = "any integer"
    elif low is not None and high is not None:
        error = f"Please enter an integer between {low} and {high}"
        situation = "both"
    else:
        error = f"Please enter an integer more than {low}"
        situation = "low only"

    while True:
        response = input(question).lower()
        if response == exit_code:
            return response

        try:
            response = int(response)

            if situation == "any integer":
                return response
            elif situation == "both":
                if low <= response <= high:
                    return response
            elif situation == "low only":
                if response >= low:
                    return response

            print(error)

        except ValueError:
            print(error)


# acceptable list of words.
emh_level = ["easy", "medium", "hard"]

end_game = "no"
while end_game == "no":
    print()

    choose_instruction = "What level do you want to play? "
    choose_error = "Please choose from easy/medium/hard (or xxx to quit)."

    difficulty = input(choose_instruction).lower()

    # end of game if exit code is typed
    if difficulty == "xxx":
        break

    while difficulty not in emh_level and difficulty != "xxx":
        print(choose_error)
        difficulty = input(choose_instruction).lower()

    # generated algebra questions for each level
    def play_round(difficulty):
        if difficulty == "easy" or difficulty == "e":
            x = random.randint(1, 12)
            result = 4 * x
            question = f"What is x: 4x = {result}"

        elif difficulty == "medium" or difficulty == "m":
            x = random.randint(1, 10)
            num_one = random.randint(1, 12)
            result = num_one * x
            question = f"Find what x is: {num_one} * x = {result}"
        else:
            x = random.randint(1, 20)
            num_two = random.randint(1, 10)
            num_three = random.randint(1, 20)
            result = num_two * x + num_three
            question = f"Find what x is: {num_two}x + {num_three} = {result}"

        print(question)

        # checks if answer is correct
        user_answer = input("Your answer: ")
        if user_answer == str(x):
            print("Correct!")
            print()
            return True
        else:
            print(f"Wrong! The correct answer is {x}.")
            print()
            return True


    while True:
        success = play_round(difficulty)
        if not success:
            break

    play_again = input("Play again? (yes/no) ")
    if play_again.lower() != "yes" and play_again.lower() != "y":
        break
