# Method 1:
def circle_area(radius):  # defining a function to calculate the area of circle
    pi = 3.14  # initialize predefined value of pi
    return pi * radius ** 2   # returning area by using predefined mathematical formula 


r = float(input("Enter the radius of circle:"))  # getting input from user with the help of input() and float() functions
# float() function is used to convert given value into floating point numbers The float function (or a similar data type like double in 
# some languages) is used in circumference calculations because the result is likely to be a decimal number. The circumference formula 
# involves pi (π), which is an irrational number (a number with infinitely non-repeating decimal digits), and often the radius itself might
# also be a decimal. To ensure accurate results, variables used in the calculation (like radius, pi, and the resulting circumference) should
# be able to hold decimal values, which float (or double) provides.

Calculated_Area = circle_area(r)   # calling function with input variable as argument for passing the value to function
print("{} is the calculated area of circle.".format(Calculated_Area))  # Printing area of circle by using format() function
# uses "string formatting" in Python to print a formatted string. It replaces the placeholder {}, within the string, with the value of the
# variable Calculated_Area




    


