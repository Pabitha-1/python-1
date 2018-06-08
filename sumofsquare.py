num=int(raw_input())
ans=0
while(num!=0):
	temp=num%10
	ans=ans+(temp*temp)
	num=num//10
print(ans)
    
