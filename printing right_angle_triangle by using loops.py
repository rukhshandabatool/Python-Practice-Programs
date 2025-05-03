# Program for printing right angle triangle using loops

def print_right_angle_triangle(rows):  # defining a function to print a right angle triangle
for i in range(1, rows + 1):  # using for loop to iterate over the element
# in the outer loop 1 is the starting value of row and "row" variable holds the last value of the loop
# and loop variable "i" hold the current value of the loop; exp: in first iteration it's value is 1 "i=1"
# during 2nd "i = 2" and during 3rd "i = 3" and so on
# # point to be notice {I am using outer loop here just to iterate over the elements of row in vertical manner}
# so the outer for loop will execute until its value will be equal to the value, user will enter.
    for j in range(1, i + 1):  # then I am using inner loop to iterate over the elements of outer for loop(from 1
    # to current value of i)
    # j will hold the current value of "i", the variable of outer loop
    # this nested loop will print "*" this character in columns in horizontal manner.
    # Let's say; "i = 1" then j will hold the current value of i and " j = 1 " and one "*" character will be
    # printed.
    # "i = 2" and "j = 2" two "*" characters will be printed
    # "i = 3" and "j = 3" three "*" characters will be printed and so on
        print("* ", end="")  # here using print function to print the value
        # using "end=""" is used to enter the space between characters otherwise the second character will be
        # moved on the 2nd line like that by default:
        # *
        # *
        # * and so on, to avoid this we use end="" function to just add space so, the next character will be printed on the same line.
