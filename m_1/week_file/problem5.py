login1 = input("login")
password1 = input("password")
f = open('/home/oem/Desktop/work/database.txt' , 'r')
if login1 in f.read():
	print("login ok")
	f.close
g = open('/home/oem/Desktop/work/database.txt' , 'r')
if password1 in g.read():
	print("password ok")
	g.close

else:
	print("nujan registraciya")
	login2 = input("login")
	password2 = input("password")
	password22 = input("povtorite password")

	c = open('/home/oem/Desktop/work/database.txt' , 'r')
	if login2 not in c.read():
		if password2 not in c.read():
			if password2 == password22:
				c.close
				i = open('/home/oem/Desktop/work/database.txt' , 'a')
				i.write(f"login: {login2}, password: {password2}")
				i.close
				print ("vse uspeshno")
			else:
				print('''vvedi parol eshe raz olen'!!!''')

