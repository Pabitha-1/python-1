numbers=raw_input().split()
b=[]
for n in set(numbers):
	if numbers.count(n)>1:
		for i in n:
			b.append(i)
b.sort()
for j in b:
	print(j)
	
		
