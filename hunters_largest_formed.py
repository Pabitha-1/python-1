def large(a, b):
	ab=str(a)+str(b)
	ba=str(b)+str(a)
	return cmp(int(ba), int(ab))
l=int(raw_input())
a=[]
for i in range(l):
	c=int(raw_input())
	a.append(c)
sorted_array=sorted(a,cmp=large)
num= "".join([str(i) for i in sorted_array])
print(num)	

