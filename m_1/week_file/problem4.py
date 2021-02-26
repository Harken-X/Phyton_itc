f = open('/home/oem/Desktop/work/file.txt' , 'w')
f.write('''Python is a widely used high-level programming language for general-purpose
programming, created by Guido van Rossum and first released in 1991. An interpreted
language, Python has a design philosophy that emphasizes code readability (notably
using whitespace indentation to delimit code blocks rather than curly brackets or
keywords), and a syntax that allows programmers to express concepts in fewer lines of
code than might be used in languages such as C++ or Java.''')
f.close()

h = open('/home/oem/Desktop/work/file.txt', 'r')
t_words = []
c = (h.read().split())
for x in c:
	if "w" in x:
		t_words.append(x)
	if "w" in x:
		t_words.append(x)
print(t_words)
h.close

g = open('/home/oem/Desktop/work/file.txt', 'r')
if "w" in g.read() or "W" in g.read():
	print ("da est' ")
else:
	print ("net")
g.close()
