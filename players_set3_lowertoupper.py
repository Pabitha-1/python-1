strings=str(raw_input())
ans=''
for i in strings:
	if i.islower():
		ans=ans+i.upper()
	elif i.isupper():
		ans=ans+i.lower()
print(ans)
	
