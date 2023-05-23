w = ['apple', 'water', 'sand', 'morning', 'cherry']
with open("files\log.txt", "w", encoding="utf - 8" ) as f:#автооткрытие и закрытие)
	#f.seek(0)
	for i in w:
		f.write(i + "\n")
	# f.write("hope")
	
	# print(f.readlines()[4])
