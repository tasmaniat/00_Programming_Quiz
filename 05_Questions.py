import random

rounds = 0
rounds_played = 0
easy_level = 0
medium_level = 0
hard_level = 0


def choice_checker(question, valid_list, error):
    valid = False
    while not valid:

        # ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # iterates through list and if response == item
        # in the list (or the first letter of an item), the
        # full item name is returned

        for var_item in valid_list:
            if response == var_item[0] or response == var_item:
                return var_item

        # output error if the item not in list
        print(error)
        print()


# List for checking responses
emh_level = ["easy", "medium", "hard"]
game_summary = 0

end_game = "no"
while end_game == "no":

    # Start of Game Play Loop
    print()
    user_choice = choice_checker("What level would you like to play? ",
                                 emh_level,
                                 "Please choose Easy / Medium / Hard "
                                 "(or xxx to quit)")
    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode: " \
                  "Round {}".format(rounds_played + 1)
    else:
        heading = "Round {} of" \
                  " {} ".format(rounds_played + 1, rounds)

    choose_error = "Please choose from easy /" \
                   "medium / hard (or xxx to quit)"

    # end of game if exit code is typed
    if user_choice == "xxx":
        break

    # compare choices
    if easy_level == user_choice:
        x = random.randint(1, 10)
        coefficient = random.randint(1, 5)
        result = coefficient * x
        question = f"Find what x is: {coefficient}x = {result}"
