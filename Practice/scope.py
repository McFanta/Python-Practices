# A basic program that I made to learn and understand variable scopes

a = 7823

def happy():
    print(a)

def buddy():
    print(a)

happy()
buddy()