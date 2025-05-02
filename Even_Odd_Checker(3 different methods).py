# Method1:
def checker(number1):  # defining the function for checking the even or odd nature of input number
    if number1 % 2 == 0:  # if statement will check if the number is completely divisible by 2
        return "Number is even."  # if the number is divisible it will return a string "Number is even."
    else:                # if number is not completely divisible by 2 then else statement will be executed and it
        # will return a string "Number is odd."
        return "Number is odd."


Number = int(input("Enter a number:"))   # declaring a variable and getting input from user by using input() and int()
# functions
result = checker(Number)                 # Calling function "checker" by passing "Number" variable value as a parameter
print("Result", str(result))          # Finally, printing the result by using str() function


# Method2:
def even_odd_checker(number2):  # defining a function and passing it a parameter
    if number2 % 2 != 0:        # if the value of parameter of function divided by 2 is not equal to zero then it will
        # return that "Odd" means, the given number is odd
        return "odd"
    else:                       # if, if condition isn't true then else condition will be executed and will return
        # "Even" means, the given number is even
        return "Even"


number = int(input("Enter a number:"))  # declaring a variable and getting input by using input() function and int()
checking_Result = even_odd_checker(number)  # calling the function and passing the input value as a parameter and
# assigning the final result to another variable called "checking_Result"
print(checking_Result)  # Finally, printing the result


# Method3:
def even_odd_checker(number2):  # defining a function and passing it a parameter
    if number2 % 2 != 0:        # if the value of parameter of function divided by 2 is not equal to zero then it will
        # return that "Odd" means, the given number is odd
        return "odd"
    else:                       # if, if condition isn't true then else condition will be executed and will return
        # "Even" means, the given number is even
        return "Even"


number = 2  # declaring a variable and getting input by using input() function and int()
print("Result: " + even_odd_checker(number))  # calling the function and passing the input value as a parameter and
# printing the result
