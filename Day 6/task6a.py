# Python Program to Print the Fibonacci sequence
terms = int(input("Enter the number of terms: "))
n1, n2 = 0, 1
count = 0
if terms <= 0:
   print("Please enter a positive integer")
elif terms == 1:
   print("Fibonacci sequence upto",terms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < terms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

# Explain Armstrong number and write a code with a function
# Armstrong Number - an armstrong number in a given number base b is a number
# that is the sum of its own digits each raised to the power of the number of digits.
num = int(input("Enter a number: "))
sum = 0
# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

# Write a program to print the multiplication table of 9
num = 9
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)

# Check if a program is negative or positive
num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")