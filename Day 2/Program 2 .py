n = int (input (" enter the value of n:"))
a = 0
b = 1
print ("the fibonacci series upto ",n,"term")
for i in range (n) :
	print(a, end =" ")
	c = a + b
	a = b
	b = c
