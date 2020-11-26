# Exercise 1
# Write a program to create a list of n integer values and do the following
list = []
n = int(input("Enter number of elements in the list: "))
for i in range(0, n):
    element = int(input())
    list.append(element)
print(list)
# Add an item in to the list (using function)
list.insert(2, 100)
print("List after addition of an item: ")
print(list)
print('\n')
# Delete(using function)
del list[2]
print("List after deletion of an item: ")
print(list)
print('\n')
# Store the smallest number from the list to a variable
low = min(list)
print('Smallest number of the list: ')
print(low)
print('\n')
# Store the largest number from the list to a variable
high = max(list)
print('Largest number of the list: ')
print(high)
print('\n')
print("Modified List")
print(list[0:])
print('\n')

# Exercise 2 Create a tuple and print the reverse of created tuple
tuple = ('hello', '15', '3.14', 'bye', 'no')
rtuple = tuple[::-1]
print("Reverse tuple")
print(rtuple)
print('\n')

# Exercise 3 Create a tuple and convert tuple into list
list = []
tuple = ('hello', '15', '3.14', 'bye', 'no')
for i in range(5):
    list.append(tuple[i])
print("Converted list from tuple")
print(list[0:5])
