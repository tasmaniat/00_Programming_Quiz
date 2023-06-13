# Function go here...
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("please answer yes / no")


def instructions():
    print()
    print("------- WELCOME TO THE ALGEBRA QUIZ -------")
    print()
    print(" - pick a level < easy / medium / hard >\n"
          " - choose how many questions u want\n")

    print("To answer the questions correctly your goal\n "
          "is to find out what the variable 'x' is ")
    print()
    print("Example: 2x - 1 = 5   |   Example: x + 5 = 9\n"
          "          x = 3       |            x = 4")
    print()
    return ""


# Main Routine goes here...
print()
played_before = yes_no("Have you played before? ")

if played_before == "no":
    instructions()

print()
print("programs continues")
