# WA function to find out the factorial of a given number
# starting from 1 to n numbers factorial

def fact(num):
    result = 1
    for i in range(num):
        result = result * num
        num -= 1
    return result
n = int(input("Enter how many number/'s factorial u want:"))
for i in range(1, n+1):
    print('Factorial of', i, 'is:', fact(i))