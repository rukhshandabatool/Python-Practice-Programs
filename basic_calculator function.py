#  Write a function that takes two numbers and an optional operator (+, -, *, /) and returns the result
#  of the operation. If no operator is provided, return the sum.
def calculation(num1, num2, operator):
    if operator == "+":     # if condition to check if the input operator is "+"
        return num1 + num2  # if true then num1 & num2 will be added else, move to the next statement
    elif operator == "-":   # elif condition to check if the input operator is "-"
        return num1 - num2  # if true then num1 & num2 will be subtracted else, move to the next statement
    elif operator == "*":   # elif condition to check if the input operator is "*"
        return num1 * num2  # if true then num1 & num2 will be multiplied else, move to the next statement
    elif operator == "/":   # elif condition to check if the input operator is "/"
        return num1 / num2  # if true then num1 & num2 will be divided else, move to the next statement
    else:                   # If, all the if statements are false then else condition will be executed
        return num1 + num2  # sum of both numbers


number1, number2 = int(input("Enter 1st number: ")), int(input("Enter 2nd number: "))
# input prompts for getting numbers
input_operator = input("Enter operator according to your choice: ")  # getting required operator
result = calculation(number1, number2, input_operator)  # calculating result by passing the arguments(values) through
# variables number1 & number2
print("The calculation result is: " + str(result))
# finally printing the result by using print() and str() functions
