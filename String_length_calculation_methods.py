# Different ways to calculate the length of the string

# Method 1 (Direct printing)
STRING = input("Enter a string:")  # declaring a variable and getting input
print(len(STRING))  # printing the length of the string
print()

# Method 2 (by assigning the length to a variable)
STRING1 = input("Enter a string:")
string_length = len(STRING1)  # Declaring a variable and initializing it to the length of the input string variable
print("length of string:", len(STRING1))  # printing the length of the string again
print("The length of string is equals to:", str(string_length))  # printing the string
print()

# Method 3 (by using a predefined string)
string = "I AM A STUDENT IN IT FACULTY."  # Declaring and initializing the  variable to string
print("The string length is:", str(len(string)))  # printing the string
print(len(string))  # printing the length again
