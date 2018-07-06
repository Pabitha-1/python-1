def kLargest(arr, k):
	arr.sort(reverse=True)
	for i in range(k):
		print (arr[i]) 
a,k=raw_input().split()	
a=int(a)
k=int(k)
arr=[]
for i in range(int(a)):
	b=int(raw_input())
	arr.append(b)
kLargest(arr, k)
