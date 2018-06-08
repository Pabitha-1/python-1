def fact(n):
	if(n==1):
		return 1
	else:
		
		return n*fact(n-1)
number=int(raw_input())
if(number<0):
	print("invalid data")
elif(number==0):
	print(1)
else:
	print(fact(number))
	
