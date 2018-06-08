s=[]
n=int(raw_input())
for i in range(n):
	c=raw_input()
	s.append(c)
m=0
t="kabali"
t=(''.join(sorted(t)))
for a in s:
	if len(a)==len(t):
		a=(''.join(sorted(a)))
		if a==t:
			m=m+1
print(m)
