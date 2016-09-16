# A fun little game that I made for fun and to be more familiar with more functions

def rock_paper_scissors():
    action = 'Welcome to rock, paper and scissors!'
    print action
rock_paper_scissors()

def match_info():
    print("This match is between You and the computer.")
    print("You can use a rock, a paper and a scissor")
    print("Good Luck!")
match_info()

def game_event():
    action = raw_input("Rock, paper, Scissors ")
game_event()

def final_event():
    import random
    foo = ['You Won!', 'The computer Won!', 'Tie Between Johannes and the computer!']
    print(random.choice(foo))
final_event()