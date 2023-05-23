import random

# array = ['ь','ъ','ы','ый','й']
def reads_cities(): 
    with open('cities.txt', "r", encoding='utf-8') as f: 
        a = [i.rstrip("\n").lower() for i in f.readlines()]
    return list(filter(lambda x: (x), a))
def get_random_citt(y):
    s = reads_cities()
    return random.choice(list(filter(lambda x: (x.startswith(y)), s)))
# def exceptions(x):
#     return city[-1].isalpha() and city[-1] not in array

        
