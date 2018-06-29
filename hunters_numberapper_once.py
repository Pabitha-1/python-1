ab=int(raw_input())
c=[]
for i in range(ab):
	d=int(raw_input())
	c.append(d)
for j in set(c):
	new=(c.count(j))
if(new==1):
	print(j)
	
	
