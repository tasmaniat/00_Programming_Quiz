import random


def generate_algebra_question():
    x = random.randint(1, 12)
    operator = random.choice(['+', '-', '*', '/'])

    if operator == '/':
        divisor = random.randint(1, 10)
        dividend = x * divisor
        question = f"What is x: {dividend} / {divisor} = x"
        answer = str(x)
    else:
        operand = random.randint(1, 50)
        if operator == '+':
            result = operand + x
        elif operator == '-':
            result = operand - x
        elif operator == '*':
            result = operand * x

        question = f"What is x: {operand} {operator} x = {result}"
        answer = str(x)

    return question, answer


# Generate 5 algebra questions
for _ in range(5):
    question, answer = generate_algebra_question()
    print(question)
    user_answer = input("Your answer: ")
    if user_answer == answer:
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is {answer}.")
    print()
