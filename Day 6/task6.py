# Write a program to loop through a list of numbers and add +2 to every value to elements in list
original_list = [15, 20, 85, 152, 305, 500]
print("The original list is : " + str(original_list))
# using list comprehension
# adding K to each element
res = [x + 2 for x in original_list]
# printing result
print("The list after adding 2 to each element : " + str(res))

# Write a program to get the below pattern
for i in range(5, 0,-1):
    for j in range(i, 0,-1):
        print(j, end = '')
    print('\n')
print()
