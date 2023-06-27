rounds_played = 0
rounds_incorrect = 0
rounds_skipped = 0

# Results for testing purposes
test_results = [True, False, False, True, True]

for item in test_results:
    rounds_played += 1

    # Checks answer user inputs
    result = item

    if result:
        # Correct answer
        print("Correct!")
    else:
        # Incorrect answer
        rounds_incorrect += 1
        print("Incorrect!")

# Quick Calculations (stats)
rounds_won = rounds_played - rounds_incorrect - rounds_skipped

# End of game statements
print()
print('--------------- End Game Summary ---------------')
print("Correct: {} \t|\t Incorrect: {} \t|\t Skipped: "
      "{}".format(rounds_won, rounds_incorrect, rounds_skipped))
print('------------------------------------------------')
print()
print("Thanks for playing")
