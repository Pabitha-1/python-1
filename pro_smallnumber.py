num1=int(raw_input())
num2=int(raw_input())
var=list(str(num1))
e=num2
while e>0:
    e=e-1
    del(var[e])
print(''.join(var))
