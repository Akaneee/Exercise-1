num=input("Place a number: ")
sum=num
for i in range(1, num):
    sum=sum*(num-i)
print "Factorial of", num, "is", sum
