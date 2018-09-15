str=str(raw_input())
a=list(str)
for i in range(len(a)):
	if a[i]==' ':
		a[i]=''
ans=''
for i in a:
	ans=ans+i
print(ans.strip())
