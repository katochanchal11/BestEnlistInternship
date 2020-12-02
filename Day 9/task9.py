# Exercise 1 - Create a lambda function that multiplies argument x with argument y
a = lambda u, v : u * v
print(a(20, 30))

# Exercise 2 - Write a Python program to create Fibonacci series to n using Lambda
def fibonacci(count):
    listA = [0, 1]
    any(map(lambda _:listA.append(sum(listA[-2:])),
         range(2, count)))
    return listA[:count]
print("Enter number of terms: ")
print(fibonacci(int(input())))
print('\n')

# Exercise 3 - Write a Python program that multiply each number of given list with a given number
numbers = [12, 25, 89, 100, 205]
value = 5
print("Given List: ", numbers)
print("Given number: ", value)
multiply_numbers=list(map(lambda numbers : numbers * value, numbers))
print('Updated List: ',' '.join(map(str,multiply_numbers)))
print('\n')

# Exercise 4 - Write a Python program to find numbers divisible by 9 from a list of numbers
new_list = [9, 18, 27, 35, 45, 55, 63, 73, 81, 99, 100]
result = list(filter(lambda x: (x % 9 == 0), new_list))
print("Numbers divisible by 9 are",result)

# Exercise 5 - Write a Python program to count the even numbers in a given list of integers
my_list = [1, 2, 3, 5, 7, 8, 9, -10, 11, 12, -13, 14, 15, -3, 0, 4]
print("\nGiven List of Numbers:",my_list)
find_even = len(list(filter(lambda x: (x % 2 == 0) , my_list)))
find_odd = len(list(filter(lambda x: (x % 2 != 0) , my_list)))

print("\nNumber of even numbers in the given list: ", find_even)
print("\nNumber of odd numbers in the given list: ", find_odd)
