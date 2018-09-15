var,vari=raw_input().split()
var=int(var)
vari=int(vari)
count=0
if var > 1:
	for i in range(var,vari+1):
		if((i==2) or (i%2!=0) and (i!=9)):
			count+=1
		else:
			
			i=i+1
			
	print count	
