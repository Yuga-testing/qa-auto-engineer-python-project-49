from brain_games.scripts.games.brain_calc import question_br_calc, br_calc

from brain_games.scripts.games.brain_even import question_br_even, br_even

from brain_games.scripts.games.brain_gcd import question_br_gcd, br_gcd

from brain_games.scripts.games.brain_progression import question_br_progression, br_progression


import prompt

def main():
    command = str(input("Input name of the game:  "))
    if command in ["brain-games", "brain-even", "brain-calc", "brain-gcd", "brain-progression"]:
       print("Welcome to the Brain Games!")
       name = prompt.string("May I have your name? ")
       print("Hello, " + name + "!")

       match command:
           case "brain-even":
               question_br_even()
           case "brain-calc":
               question_br_calc()
           case "brain-gcd":
               question_br_gcd()
           case "brain-progression":
               question_br_progression()

       def start_main():
           i = 1
           while i < 4:
               match command:
                   case "brain-even":
                       i = br_even(name, i)
                   case "brain-calc":
                       i = br_calc(name, i)
                   case "brain-gcd":
                       i = br_gcd(name, i)
                   case "brain-progression":
                       i = br_progression(name, i)
           if i == 4:
               return print("Congratulations, " + name + "!")

       start_main()
    else:
       print("try again")

if __name__ == "__main__":
    main()    