def find_largest_number(n1, n2, n3):  # Define a function and pass it three parameters to hold the values to perform the
    # operation of if-else statements
    if n1 >= n2 and n1 > n3:  # this if condition is using two scenarios two check if n1 is greater than both n2 & n3
        return "n1 is greater."  # if greater than this string will be return
    elif n2 >= n1 and n2 >= n3:  # this if condition is using two scenarios two check if n2 is greater than both n1 & n3
        return "n2 is greater."  # if greater than this string will be return
    else:                        # If both conditions given above are false then this statement will be executed which
        # means n3 is greater
        return "n3 is greater."  # this string will be return


num1, num2, num3 = int(input("Enter 1st number: ")), int(input("Enter 2nd number: ")), int(input("Enter 3rd number: "))
# declaring three variables and getting input from the user
print(find_largest_number(num1, num2, num3))  # calling the function by passing three values through variables to
# parameters of functions.
