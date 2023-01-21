# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word
import random
# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
# pick one word randomly from the sequence
word = random.choice(WORDS)
# create a variable to use later to see if the guess is correct
correct = word
# create a jumbled version of the word
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
# start the game
print(
"""
 Welcome to Word Jumble!
 Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)
score=20
time=1
print("The jumble is:", jumble.upper())
hint=input("Do you want a hint if you pick hint you will lose 5 points\nyes or press any button to continue\n")
if hint=="yes":
    score-=5
    if correct=="python":
        p="One of the most deadly reptiles in the world", "If i say monty what should you say_____"  , "I have dangerous fangs"
        print(random.choice(p))
    elif correct=="jumble":
        j="What game are you playing" , "Starts with a J and ends with a E"
        print(random.choice(j))
    elif correct=="difficult":
        d="This word describes rocket science" , "Starts with a 'D' and ends with a 'T'"
        print(random.choice(d))
    elif correct=="easy":
        e="What is the opposite of difficult" , "Starts with a 'E"
        print(random.choice(e))
    elif correct=="answer":
        a="Synonymical to solution" , "Starts with a 'A" , "Its middle letters are 'S' and 'W'"
        print(random.choice(a))
    elif correct=="xylophone":
        print("A drum that makes music")
else:
 score+=0
guess = input("\nYour guess: ")
while guess != correct and guess != "":
 print("Sorry, that's not it.")
 guess = input("Your guess: ")
 time+=1
if guess == correct:
     print("That's it! You guessed it!\n")
     score+=5
print("Your final score is ",score-(time-1),"Goodjob meistro")
print("Thanks for playing.")