# A funny program that calculates the allowed age limit of girls I can date

def allowed_dating_age(my_age):
    girls_age = my_age / 2 + 6
    return girls_age

johannes_limit = allowed_dating_age(14)
print("Johannes can date", johannes_limit, "year old girls or older")
