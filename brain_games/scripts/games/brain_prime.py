import random

from brain_games.answer_yes_no import answer_false, answer_true


def question_br_prime():
    print("Answer 'yes' if given number is prime. Otherwise answer 'no'.")


def is_prime(num):
    if num < 2: 
        return False
    for k in range(2, int((num / 2)) + 1):
        if num % k == 0:
            return False
    return True


def br_prime(name, i):
    num = random.randint(1, 100)
    print("Question: " + str(num))
    answer = str(input("Your answer: ").lower().strip())
    if is_prime(num):
        i = answer_true(name, answer, i)
    else:
        i = answer_false(name, answer, i)
    return i
