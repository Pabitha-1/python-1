count={}
string=str(raw_input())
for s in string:
	if s in count.keys():
		count[s]+=1
	else:
		count[s]=1
for key in count:
	if count[key]>1:
		
		print(key)
