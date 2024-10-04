# Python 3 program to check the number is 
# divisible by all digits are not.

n = 128
x = str(n)
a = list(map(int, x))
c = 0
for i in a:
	if(n % i == 0):
		c += 1
if(c == len(a)):
	print("Yes")
else:
	print("No")
