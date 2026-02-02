import random


def question_br_even():
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")


def is_even(num):
    return num % 2 == 0


def br_even_main(name, i):
    num = random.randint(1, 100)
    print("Question: " + str(num))
    answer = str(input("Your answer: ").lower().strip())
    if is_even(num):
        match answer:
            case "yes":
                print("Correct!")
                i += 1
                return i
            case _:
                print(
                     "'" + answer 
                    + "'" 
                    + "is wrong answer ;(. Correct answer was 'yes'."
                )
                i = 4
                print("Let's try again, " + name + "!")
                return i
    else:
        match answer:
            case "no":
                print("Correct!")
                i += 1
                return i
            case _:
                print(
                    "'" + answer 
                    + "'" 
                    + "is wrong answer ;(. Correct answer was 'no'."
                )
                i = 5
                print("Let's try again, " + name + "!")
                return i
