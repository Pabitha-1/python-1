a=int(raw_input())
b=raw_input().split()
c=b[:a]
s=0
g=[]
try:
	for i in range(0,len(c)):
		s=s+int(c[i])
		if(s>0):
			r=s
			g.append(r)	
	print max(g)
except:
	print("invalid")
