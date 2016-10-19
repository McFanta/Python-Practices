# A funny program that tells you who I can date

def girls_I_can_date():
    import random
    girls = ['Camilla', 'Sara', 'Sofie', 'Sophie', 'Marielle']
    guy = "Johannes"
    print(guy, "can date", random.choice(girls))
girls_I_can_date()
