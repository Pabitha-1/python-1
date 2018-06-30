a,b=raw_input().split()
a=int(a)
b=int(b)
c=[]
for i in range(a):
	g=int(raw_input())
	c.append(g)
h=int(raw_input())
if(h in c):
	print("Yes")
else:
	print("No")
