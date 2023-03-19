# program to print first 10 Numbers
i = 1
for i in range(1, 11):
    print(i)

# program to calculate the sum of first 10 natural number.
i = 1
a = 0
for i in range(1, 11):
    a = i + a

print(f'sum of first 10 Natural Numbers is', a)
print("********************************************************************")


J = input(f'Input the value to generate multiplication ')
a = int(J)
for i in range(1, 11):
    num = a*i
    print(f'{a} X {i} = {num}' )
    # print(a*i)

# Write a program to find the factorial value of any number entered through the keyboard.
# 3! 3*2*1 , 4! 4*3*2*1

factorial = input(f'enter a number for which you want to find the factorial ')
factorial = int(factorial)
result = factorial
for i in range(1, factorial):
    result = result * (factorial-i)

print(f'Factorial of {factorial} is', result)





