import math
#D=b²-4ac
b=float(input("b"))
a=float(input("a"))
c=float(input("c"))
D=((b** 2)-4*a*c)
print(D)
if D > 0:
	#x1,2=(b ± √D) /2a
	x1=(b+ (math.sqrt(D)) /2*a)
	x2=(b- (math.sqrt(D)) /2*a)
	print(x1,x2)
elif D==0:
	x= (-D / 2*a)
	print(x)
else:
	print('Корней нету')	
