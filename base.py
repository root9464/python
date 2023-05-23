from kodland_db import db
# io = db.tasks.get_all()
# for i in io:

# i = db.tasks.get("id", 2)

# if i:
#     print(i.id, i.description)
# else:
#     print('poshel won')
# p = input("ВВоди")
# o = {
#     'description' : p,
#     'minutes' : i.minutes,
# }
# db.tasks.put(o)

db.tasks.update('id', 3,"id", 1)