import random

def hangman(word):
    wrong = 0
    stages = ["",
        "_______________   ",
        "|         |       ",
        "|         |       ",
        "|         |       ",
        "|         0       ",
        "|        /|\      ",
        "|        / \      ",
        "|______________   "
        ]

    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")
    #print(stages)

    while wrong < len(stages):
        guess = input("Please enter your character: ")
        if guess in rletters:
            print("You are right!")
            board[rletters.index(guess)] = guess
            print("The word is " + str(board))
            rletters[rletters.index(guess)] = '$'
            if '_' not in board:
                win = True
        else:
            print("You are wrong!")
            for i in range(wrong + 1):
                print(stages[i])
            wrong += 1
        if win == True:
            print("You win!")
            print("The correct word is " + word.upper() + "!")
            break
    if not win:
        print("You lose!")
        print("The correct word is " + word.upper() + "!")

def word_select():
    words = ['cat', 'dog', 'rabbit']
    i = random.randint(0, len(words)-1)
    return words[i]


hangman(word_select())
