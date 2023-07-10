game_summary = []

rounds_played = 5
best_score = float('inf')
worst_score = float('-inf')
average_score = 0
rounds_correct = 0
rounds_incorrect = 0
total_score = 0

for item in range(1, rounds_played + 1):
    result = input("Enter the result for question {}: ".format(item)).strip()

    # Compares the answer with the correct answer for each question
    outcome = "correct answer".format(item, result)

    if result == "correct":
        rounds_correct += 1
    elif result == "":
        result = "skipped"
    else:
        result = "incorrect"
        rounds_incorrect += 1

    score = int(input("Enter the score for round {}: ".format(item)))
    total_score += score

    if score < best_score:
        best_score = score

    if score > worst_score:
        worst_score = score

    game_summary.append((item, result, score))

# Calculate game statistics
average_score = total_score / rounds_played if rounds_played != 0 else 0

if rounds_played == 0:
    percent_correct = 0
else:
    percent_correct = rounds_correct / rounds_played * 100

percent_incorrect = rounds_incorrect / rounds_played * 100 if rounds_played != 0 else 0

# Calculates the game statistics such as average score,
# percentage of correct answers, and percentage of incorrect answers.
print()
print("----------------------------")
print("Correct: {}\t|\tIncorrect: {} ".format(rounds_correct, rounds_incorrect, ))
print("----------------------------")
print()

# Prints the number of correct and incorrect answers.
print()
print("************ Quiz Scores ***********")
print("Question\t| Result\t\t| Score")
print()
for item, result, score in game_summary:
    print("{}\t\t\t| {}\t\t| {}".format(item, result, score))

# Prints the scores for each question in the quiz.
print("\n******** Summary Statistics ********")
print("Best Score: {}\nWorst Score: {}\nAverage Score: {:.2f}"
      .format(best_score, worst_score, average_score))
