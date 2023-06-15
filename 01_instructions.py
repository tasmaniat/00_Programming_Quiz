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

    print(" You will be shown an equation to solve")
    print()
    print("To answer the questions correctly your goal\n"
          "is to find out what the variable 'x' is. ")
    print()
    print("Example (easy):    |  Example (medium):\n"
          "if a=2 what is x?  |  what is 'x'   \n"
          "   a + x = 5       |   8 * x = 56\n"
          "       x = 3       |       x = 7 \n")
    print()
    return ""


# Main Routine goes here...
print()
played_before = yes_no("Have you played before? ")

if played_before == "no":
    instructions()

print()
print("programs continues")
