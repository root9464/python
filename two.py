

m = [ ]
with open("files\log.txt", "r+", encoding="utf-8") as f:

    for i in f.readlines(): 
        r = int(i.strip())
        m.append(r)

    #result = [int(item.rstrip()) for item in f.readlines()]

print("Сумма обьектов в файле =",sum(result))
    