import random

num1 = random.randint(1,6)
num2 = random.randint(1,6)
num3 = random.randint(1,6)
print("The first number : " + str(num1))
print("The second number : " + str(num2))
print("The third number : " + str(num3))
num1_IsEven = num1 % 2 == 0
num2_IsEven = num2 % 2 == 0
num3_IsEven = num2 % 2 == 0

all_even_odd = num1_IsEven == num2_IsEven

print(all_even_odd)




