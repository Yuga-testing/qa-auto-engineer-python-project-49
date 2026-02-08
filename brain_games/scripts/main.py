import prompt

from brain_games.games.brain_calc import br_calc, question_br_calc
from brain_games.games.brain_even import br_even, question_br_even
from brain_games.games.brain_gcd import br_gcd, question_br_gcd
from brain_games.games.brain_prime import br_prime, question_br_prime
from brain_games.games.brain_progression import (
    br_progression,
    question_br_progression,
)


def main():
    games = {
        "brain-even": (question_br_even, br_even),
        "brain-calc": (question_br_calc, br_calc),
        "brain-gcd": (question_br_gcd, br_gcd),
        "brain-progression": (question_br_progression, br_progression),
        "brain-prime": (question_br_prime, br_prime),
    }

    command = str(input())

    if command in games or command.startswith("brain-games"):
        print("Welcome to the Brain Games!")
        name = prompt.string("May I have your name? ")
        print("Hello, " + name + "!")
        
    else:
        print("Welcome to the Brain Games!")
        #print("try again")
        return
    
    if command.startswith("brain-games"):
        exit()

    show_rules, play_round = games[command]
    show_rules()

    i = 1
    while i < 4:
        i = play_round(name, i)
    if i == 4:
        return print("Congratulations, " + name + "!")


if __name__ == "__main__":
    main()    