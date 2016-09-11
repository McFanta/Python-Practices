# A fun little game that I made for fun and to be more familiar with more functions

def rock_paper_scissors():
    action = 'Welcome to rock, paper and scissors!'
    print action
rock_paper_scissors()

def match_info():
    print("This match is between Johannes and Gary. Wish them luck!")
    print("You guys can use a rock, a paper and a scissor")
match_info()

def game_event():
    my_name = 'Johannes'
    action = 'used'
    my_item = 'Scissor'
    enemy_name = 'Gary'
    action = 'used'
    enemy_item = 'paper'
    if my_item is 'Scissor':
        print my_name, action, my_item
    if enemy_item is 'paper':
        print enemy_name, action, enemy_item
game_event()

def final_action(winner = 'Johannes'):
    if winner is 'Johannes':
        print winner, "won the match!"
    elif winner is 'Unknown':
        print("Tie between Johannes and Gary!")
final_action()