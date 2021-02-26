i = -100
a = 0

while i<=100 :
	if i%13==0:
		if i%2==0:
			print(i,i**2)
			a+=1
	i+=1
print(a)
print('''---------------------------------------------''')
t = -100
b = 0
while t<=100 :
	if t%7==0 and t%2==0:
		
		print(t)
		b+=1
	t+=1
print(b)

