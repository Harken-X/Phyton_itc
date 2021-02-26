a = int(input('vvedite chislo'))
if a >= 100 :
	print("trehznaz")
if a >0 and a%2==0:
	print("+ and chet")
if a %31==0:
	print("na 31 bez")
if a >=100 and a%17==0 or a>150 and a==13**2:
	print("bolshe 100")
else:
	print("uslovie ne podhodit")