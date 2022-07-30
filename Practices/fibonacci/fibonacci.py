a = 0
b = 1
n = int(input("Enter the fibonacci number: "))

# Check is n is less
# than 0
if n < 0:
    print("Incorrect input")
         
# Check is n is equal
# to 0
elif n == 0:
    print(0)
       
# Check if n is equal to 1
elif n == 1:
    print(b)
else:
    for i in range(n):
        c = a + b
        a = b
        b = c
        print(c)