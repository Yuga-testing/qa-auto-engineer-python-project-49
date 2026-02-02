from brain_games.scripts.games.brain_calc import question_br_calc, br_calc_main

from brain_games.scripts.games.brain_even import question_br_even, br_even_main

from brain_games.scripts.games.brain_gcd import question_br_gcd, br_gcd


import prompt

def main():
    command = str(input("Input name of the game:  "))
    if command in ["brain-games", "brain-even", "brain-calc", "brain-gcd"]:
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

       def start_main():
           i = 1
           while i < 4:
               match command:
                   case "brain-even":
                       i = br_even_main(name, i)
                   case "brain-calc":
                       i = br_calc_main(name, i)
                   case "brain-gcd":
                       i = br_gcd(name, i)
           if i == 4:
               return print("Congratulations, " + name + "!")

       start_main()
    else:
       print("try again")

if __name__ == "__main__":
    main()    