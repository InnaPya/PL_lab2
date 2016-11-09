a = open("access.log", 'r')
b = a.read()
import re
c = re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', b)
dict = {}
for i in c:
	if i in dict:
		dict[i] += 1
	else:
		dict[i] = 1
d = ""
for i in sorted(dict):
	g = re.match('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', i)
	if g.group(0) != d:
		print()
		print(g.group(0))
		d = g.group(0)
	print(i, "-", dict[i])

	


