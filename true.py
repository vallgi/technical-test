# Write a program that takes an integer as input and returns true if the input is a power of two.
 
num = int(input("Enter a number: "))

def isPowerOfTwo(num):
    if num == 0:
        return False
    while num != 1:
        if num % 2 != 0:
            return False
        num = num // 2
        return True

if isPowerOfTwo(num):
    print("True")
else:
    print("False")