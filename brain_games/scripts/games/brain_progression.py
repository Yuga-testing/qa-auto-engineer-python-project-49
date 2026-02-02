import random

from brain_games.wrong_answer import wrong_answer


def question_br_progression():
    print("What number is missing in the progression?")

def progression_elements(len_progression, progression, start, step):
    for k in range(len_progression):
        element = start + k * step
        progression.append(element)


def br_progression(name, i):
    len_progression = 10
    progression = []
    start = random.randint(1, 20)
    step = random.randint(1, 20)
    progression_elements(len_progression, progression, start, step)
    index_unknown_el = random.randint(1, len_progression-1)
    result = progression[index_unknown_el]
    progression_unknown = progression.copy()
    progression_unknown[index_unknown_el] = ".."
    print(f'Question:', *progression_unknown)
    answer = int(input("Your answer: "))
    if answer == result:
        print("Correct!")
        i += 1
        return i
    else:
        wrong_answer(name, answer, result)
        i = 5
        return i
