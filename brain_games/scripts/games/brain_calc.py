import random

from brain_games.wrong_answer import wrong_answer


def question_br_calc():
    print("What is the result of the expression?")


def br_calc(name, i):
    num_1 = random.randint(1, 50)
    num_2 = random.randint(1, 50)
    operation = random.choice("+-*")
    print("Question: " + str(num_1) + " " + operation + " " + str(num_2))
    answer = int(input("Your answer: "))
    match operation:
        case "+":
            result = num_1 + num_2
        case "-":
            result = num_1 - num_2
        case "*":
            result = num_1 * num_2
    if answer == result:
        print("Correct!")
        i += 1
        return i
    else:
        wrong_answer(name, answer, result)
        i = 5
        return i

