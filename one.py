import random
import os
import time
s = [ ]
w = 60 #значения лабиринта
h = 16
for i in range(0, h): #генерация
        line = []
        for j in range(0, w):
            if i>=1 and i<h-1 and j>=1 and j<w - 1 or j == w-1:
                line.append(' ')
            else:
                line.append('*')
        s.append(line)
def draw_line(col):  #колонна (отрисовка)
    for i in range(1,h-1):
        s[i][col] = 'x'
    for i in range(random.randint(1,5)):
        z = random.randint(1,h-2)
        s[z][col] = " "
for i in range(1,w): #отрисовка коллон
    if i%2 == 0:
         draw_line(i)
x = 0 #чертика
y = 1
s[x][y] = "+"
while True: #условия
    for i in s:
        for j in i:
            print(j, end=" ")
        print()
    d = input("Движение:")
    if d == "st":
        break
    s[x][y] = " "
    if d == 'w' or d == "ц":
        x += 1
    elif d == "s" or d == "ы":
        x -= 1
    elif d == "d" or d == "в":
        y += 1
    elif d == "a" or d == "ф":
        y -= 1
    if s[x][y] == 'x' or s[x][y] == "*" :
        os.system('cls')
        time.sleep(2)
        print('Sorry you loser))))')
        break
    elif y == w-2:
        os.system('cls')
        print('you win')
        break
    s[x][y] = '+'
    os.system('cls')