# Write a program to convert the number of days to ages
days_in_a_week = 7
# Function to find
# year, week, days
def find(number_of_days):
    year = int(number_of_days / 365)
    week = int((number_of_days % 365) /
               days_in_a_week)
    days = (number_of_days % 365) % days_in_a_week
    print("years = ", year,
          "\nweeks = ", week,
          "\ndays = ", days)
number_of_days = 500
find(number_of_days)

# Solve Trigonometry problem using math function write a program to solve us-ing math function
# sin() and cos()
import math
a = math.pi/10
print ("The value of sine of pi/10 is : ", end="")
print (math.sin(a))
print ("The value of cosine of pi/10 is : ", end="")
print (math.cos(a))

