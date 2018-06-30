a=int(raw_input())
c=[]
g=[]
for i in range(a):
	ab=int(raw_input())
	c.append(ab)
for j in range(a):
	if((j%2==0) and (c[j]%2!=0)):
		g.append(c[j])
	elif((j%2!=0) and (c[j]%2==0)):
		g.append(c[j])
print(g)		
