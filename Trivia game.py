"""Trivia Game"""

import question


def main():
    question1 = question.Question("How many colours are there in a rainbow? ", "A. 3", "B. 5", "C. 6", "D. 7", "D")
    question2 = question.Question("When did the world celebrate it's most recent millennium? ", "A. Year 1900",
                                  "B. Year 2000", "C. Year 1800", "D. Year 1950", "B")
    question3 = question.Question("How many degrees are found in a circle? ", "A. 250", "B. 345", "C. 360", "D. 270",
                                  "C")
    question4 = question.Question("How many squares are there on a chess board? ", "A. 64", "B. 48", "C. 60", "D. 36",
                                  "A")
    question5 = question.Question("How many points does a compass have? ", "A. 28", "B. 36", "C. 32", "D. 48", "C")

    player1 = 0
    player2 = 0

    set_1 = [question1, question2]
    set_2 = [question3, question4]
    set_3 = [question5]

    print("Player 1: ")
    for query in set_1:
        print("\n")
        print(query.get_question())
        print(query.get_answer1())
        print(query.get_answer2())
        print(query.get_answer3())
        print(query.get_answer4())
        guess = input("Please enter the letter of the correct answer:    ")
        if guess.upper() == query.get_answer():
            print("You are right!")
            player1 += 1
        else:
            print("You are wrong!")

    for query in set_2:
        print("\n")
        print(query.get_question())
        print(query.get_answer1())
        print(query.get_answer2())
        print(query.get_answer3())
        print(query.get_answer4())
        guess = input("Please enter the letter of the correct answer:    ")
        if guess.upper() == query.get_answer():
            print("You are right!")
            player1 += 1
        else:
            print("You are wrong")

    for query in set_3:
        print("\n")
        print(query.get_question())
        print(query.get_answer1())
        print(query.get_answer2())
        print(query.get_answer3())
        print(query.get_answer4())
        guess = input("Please enter the letter of the correct answer:    ")
        if guess.upper() == query.get_answer():
            print("You are right!")
            player1 += 1
        else:
            print("You are wrong")

    print("Player 1 earned: " + str(player1) + " points. ")

    print("player 2: ")
    for query in set_1:
        print("\n")
        print(query.get_question())
        print(query.get_answer1())
        print(query.get_answer2())
        print(query.get_answer3())
        print(query.get_answer4())
        guess = input("Please enter the letter of the correct answer:    ")
        if guess.upper() == query.get_answer():
            print("You are right!")
            player2 += 1
        else:
            print("You are wrong")

    for query in set_2:
        print("\n")
        print(query.get_question())
        print(query.get_answer1())
        print(query.get_answer2())
        print(query.get_answer3())
        print(query.get_answer4())
        guess = input("Please enter the letter of the correct answer:    ")
        if guess.upper() == query.get_answer():
            print("You are right!")
            player2 += 1
        else:
            print("You are wrong")

    for query in set_3:
        print("\n")
        print(query.get_question())
        print(query.get_answer1())
        print(query.get_answer2())
        print(query.get_answer3())
        print(query.get_answer4())
        guess = input("Please enter the letter of the correct answer:    ")
        if guess.upper() == query.get_answer():
            print("You are right!")
            player2 += 1
        else:
            print("You are wrong")

    print("Player 2 earned: " + str(player2) + " points. ")


main()
