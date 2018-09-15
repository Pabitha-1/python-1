def rotate(a,b,c):
	r=[]
	for i in range(a-b,a):
		r.append(c[i])
	for i in range(a-b):
		r.append(c[i])
	print(r)
def main():
	try:
		a=int(input())
		b=int(input())
		c=[]
		for i in range(a):
			c.append(int(input()))
		rotate(a,b,c)
	except:
		print('invalid')
main()
