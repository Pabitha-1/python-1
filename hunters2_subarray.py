a=int(raw_input())
b=raw_input().split()
c=b[0:a]
s=0
for i in range(0,len(c)):
	s=s+int(c[i])
print(s)	
