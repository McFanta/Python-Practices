# A simple program to calculate your life expectancy

def health_calculator(age, apples_ate, cigs_smoked):
    answer = (100 - age) +(apples_ate * 3.5) - (cigs_smoked * 2)
    print(answer)

johannes_data = [14, 4, 0]

health_calculator(*johannes_data)
