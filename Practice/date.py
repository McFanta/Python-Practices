# A funny program that tells you who I can date

def girls_I_can_date():
    import random
    girls = ['Camilla', 'Sara', 'Sofie', 'Sophie', 'Marielle']
    guy = "Johannes"
    date = girls
    if date is girls:
       print guy, "can date", random.choice(girls)
    else:
        print("Sorry you don't have any girls to date!")
girls_I_can_date()
