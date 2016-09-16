# A simple program that I made to learn about flexible numbers of arguments

def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    print(total)
add_numbers(1)
add_numbers(2)
add_numbers(3)