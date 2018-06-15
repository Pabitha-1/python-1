num=int(raw_input())
g=raw_input().split()

max=-1
for i in g:
	if int(i) > int(max):
            max=i
print int(max)		
