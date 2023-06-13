# version 3 - checks that response is in a given list


# Functions go here
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


# Main routine goes here

# lists for checking responses
emh_level = ["easy", "medium", "hard", "xxx"]

# Loop for testing purposes
user_choice = ""
while user_choice != "xxx":

    # Ask user for choice and check it's valid
    print()
    user_choice = level_choice("What level would you like to "
                               "play? ", emh_level,
                               "Please choose Easy/"
                               "Medium/Hard "
                               "(or xxx to quit)")

    # print out choice for comparison purposes
    print("You chose {} Level".format(user_choice))
