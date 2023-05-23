from random import randint

def guess_number(x):
    points = 0
    number = randint(0, 10)
    guess = x
    if number == guess:
        points += 10
    else:
        points += 10 - abs(int(number - guess))
    return points, number


def dice():
    return randint(1, 4)


def twenty_one():
    result = 0
    while result <= 21:
        result += randint(0, 10)
        answ = input(f'Набрано {result} очков, продолжать?(y/n)')
        if answ == 'n':
            break
    if result > 21:
        result = 0
    return result
