import random
from time import sleep 

Cast = [
    "Bill Murray - Dr. Peter Venkman",
    "Dan Aykroyd - Dr. Raymond Stantz",
    "Harold Ramis - Dr. Egon Spengler",
    "Sigourney Weaver - Dana Barrett",
    "Rick Moranis - Louis Tullt",
    "Ernie Hudson - Winston Zeddmore"
]

Quotes = [
    "Back off, man. I'm a scientist. - Dr. Peter Venkman",
    "He slimed me. - Dr. Peter Venkman",
    "That's a big Twinkie. - Winston Zeddmore",
    "Print is dead - Dr. Egon Spengler"
]

def game():
    global Cast
    global Quotes
    anwser = input("Do you want a random cast member or quote?  ").lower()
    if anwser == ("random cast"):
        rand_cast = (random.choice(Cast))
        print(f"This is your random cast member -> {rand_cast}")
    elif anwser == ("quote"):
        rand_quote = (random.choice(Quotes))
        print(f"This is your random quote -> {rand_quote}")
    else:
        print('Please anwser the question with "random cast" or "quote" ')
        sleep(1.5)
        game()

game()

def run_game():
    q1 = input("Who was the highest paid actor in Ghostbusters?")
    while q1 != "Bill Murray":
        q1 = input("Incorrect. Who was the highest paid actor in Ghostbusters?")

run_game()
