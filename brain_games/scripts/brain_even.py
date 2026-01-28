import random

import prompt

print("Welcome to the Brain Games!")
name = prompt.string("May I have your name? ")
print("Hello, " + name + "!")
print("Answer 'yes' if the number is even, otherwise answer 'no'.")


def is_even(num):
    return num % 2 == 0


def main():
    for i in range(1, 4):
        num = random.randint(1, 100)
        print("Question: " + str(num))
        answer = str(input("Your answer: ").lower().strip())
        if is_even(num):
            if answer == "yes":
                print("Correct!")
                i += 1
            else:
                print(
                    "'" + answer 
                    + "'" 
                    + "is wrong answer ;(. Correct answer was 'yes'."
                )
                return print("Let's try again, " + name + "!")
        else:
            if answer == "no":
                print("Correct!")
                i += 1
            else:
                print(
                    "'" + answer 
                    + "'" 
                    + "is wrong answer ;(. Correct answer was 'no'."
                )
                return print("Let's try again, " + name + "!")
    return print("Congratulations, " + name + "!")


if __name__ == "__main__":
    main()
