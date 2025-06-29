# Program to calculate the average of marks

# Method 1: Simply by declaring variables without any function
obtain_marks_exam1, obtain_marks_exam2, obtain_marks_exam3 = (int(input("Enter obtain_marks of first exam:")),
                                                            int(input("Enter obtain_marks of 2nd exam:")),
                                                            int(input("Enter marks of 3rd exam:")))  # declared three
# variables and to get the information

No_of_subjects = int(input("What are the number of subjects?"))  # Getting input about the number of subjects
total_obtain_marks = obtain_marks_exam1 + total_marks_exam2 + total_marks_exam3
Average = total_obtain_marks / No_of_subjects
print("The average of marks is:", str(Average))
print("")
print("{} is the average of obtained marks.".format(Average))

# Method 2: Calculating average by declaring a function

def fun(om1, t)
