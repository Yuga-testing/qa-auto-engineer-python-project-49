import random

from brain_games.answer_yes_no import answer_false, answer_true


def question_br_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even(num):
    return num % 2 == 0


def br_even(name, i):
    num = random.randint(1, 100)
    print("Question: " + str(num))
    answer = str(input("Your answer: ").lower().strip())
    if is_even(num):
        i = answer_true(name, answer, i)
    else:
        i = answer_false(name, answer, i)
    return i
