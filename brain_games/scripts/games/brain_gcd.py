import random


from brain_games.wrong_answer import wrong_answer


def question_br_gcd():
    print("Find the greatest common divisor of given numbers.")

def br_gcd(name, i):
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    num_3 = 0
    print("Question: " + str(num_1) + " " + str(num_2))
    answer = int(input("Your answer: "))
    while num_2 != 0:
        num_3 = num_2
        num_2 = num_1 % num_3
        num_1 = num_3
        num_3 = 0
    result = num_1
    if answer == result:
        print("Correct!")
        i += 1
        return i
    else:
        wrong_answer(name, answer, result)
        i = 5
        return i

