num=int(raw_input())
g=[]
for f in range(num):
	n = int(raw_input())
	g.append(n)
max=0
for i in g:
	if i > max:
            max=i
print(max)		
