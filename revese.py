# Write a program that takes an integer as input and returns an integer with reversed digit
# ordering.


def reverse_num(input_num):
    if input_num == 0:
        return 0
    sign = -1 if input_num < 0 else 1
    num = abs(input_num)
    reversed_num = 0
    while num > 0:
        reversed_num = (reversed_num * 10) + (num % 10)
        num //= 10
    return reversed_num * sign
input_num = int(input("Enter a number: "))
print(reverse_num(input_num))



