import time

io = []
weekday = ['Пн','Вт','Ср','Чт','Пт','Сб','Вс']

print('Введите температуру')
time.sleep(0.4)

for i in weekday:
    o = int(input(f'{i}:'  ))
    io.append(o)
def test(): return round(sum(io)/len(io), 2)
print(test())
