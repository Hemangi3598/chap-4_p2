# wapp to find the sum of first  "n" +ve integers
# i/p : 5 1+2+3+4+5 = 15

num = int(input(" enter an integer "))
if num < 0:
	print("invalid integer")
else:
	sum = 0
	for i in range(1, num + 1):
		sum = sum + i
	print(" sum = ", sum)
