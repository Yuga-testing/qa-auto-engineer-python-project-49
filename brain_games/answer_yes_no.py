def answer_true(name, answer, i):
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
            i = 5
            print("Let's try again, " + name + "!")
            return i
         
         
def answer_false(name, answer, i):
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