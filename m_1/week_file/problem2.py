f = open('/home/oem/Desktop/work/file.txt' , 'w')
a = input("login")
b = input("password")
f.write(f"your name: {a}, your password: {b}")
f.close

print ({a},{b})
