def shift(a,b,c):
	r=[]
	for i in range(a-b,a):
		r.append(c[i])
	for i in range(a-b):
		r.append(c[i])
	print(r)
def main():
	try:
		a,b=raw_input().split()
		a=int(a)
		b=int(b)
		c=[]
		for i in range(a):
			c.append(int(raw_input()))
		shift(a,b,c)
	except:
		print('invalid')
main()
