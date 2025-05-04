# Program to calculate the area of circle 

def circle_area(radius):  # defining a function to calculate the area of circle
    pi = 3.14  # initialize predefined value of pi
    return pi * radius ** 2   # returning area by using predefined mathematical formula 


r = float(input("Enter the radius of circle:"))  # getting input from user with the help of input() and float() functions
Calculated_Area = circle_area(r)   # calling function with input variable as argument for passing the value to function
print("{} is the calculated area of circle.".format(Calculated_Area))  # Printing area of circle by using format() function





    


