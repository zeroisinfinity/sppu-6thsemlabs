# ============================================================
# QUESTION:
# Develop an elementary chatbot for any suitable
# customer interaction application.
# ============================================================


# ============================================================
# EXPLANATION:
#
# A chatbot is a program that simulates conversation
# with users.
#
# This chatbot:
#
# 1. Greets user
# 2. Asks user's name
# 3. Guesses age
# 4. Counts numbers
# 5. Asks quiz question
# 6. Ends program
#
# It uses:
# - Functions
# - Input/output
# - Loops
# ============================================================


# ============================================================
# EXPLANATION WITH EXAMPLE:
#
# Example Interaction:
#
# Bot: Hello! My name is TE-Chatbot.
# User enters name.
#
# Bot guesses age using remainders.
#
# Bot counts numbers.
#
# Bot asks programming question.
#
# Bot prints congratulations.
# ============================================================


# ======================
# CHATBOT PROGRAM
# ======================

def greet(bot_name, birth_year):

    print("Hello! My name is", bot_name)

    print("I was created in", birth_year)


def remind_name():

    print("Please remind me your name:")

    name = input()

    print("What a great name you have,", name)


def guess_age():

    print("Enter remainders of your age by 3,5 and 7:")

    rem3 = int(input())

    rem5 = int(input())

    rem7 = int(input())

    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is:", age)


def count():

    print("Enter number to count:")

    num = int(input())

    counter = 0

    while counter <= num:

        print(counter)

        counter += 1


def test():

    print("Why do we use methods?")

    print("1. To repeat statements")

    print("2. To divide program")

    print("3. To check execution time")

    print("4. To interrupt program")

    answer = 2

    guess = int(input())

    while guess != answer:

        print("Try again")

        guess = int(input())


    print("Correct!")


def end():

    print("Congratulations!")


greet('TE-Chatbot', '2022')

remind_name()

guess_age()

count()

test()

end()