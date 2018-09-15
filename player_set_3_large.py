num1,num2=raw_input().split()
num1=int(num1)
num2=int(num2)
maximum=1
for x in range(1,min(num1,num2)+1):
	if num1%x==0 and num2%x==0:
		if x>maximum:
			maximum=x
print maximum
