a=int(raw_input())
c=[]
b=[]
for i in range(a):
	numbers=int(raw_input())
	c.append(numbers)
for n in set(c):
	if c.count(n)>1:
		b.append(n)
b.sort()
for j in b:
	print(j)
	
	
