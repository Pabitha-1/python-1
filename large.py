a,b,c=raw_input().split()
if((a>b)and(a>c)):
	large=a
elif((b>a)and(b>c)):
	large=b
else:
	large=c
print (large)
