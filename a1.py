#getting the values
labs_completed = int(input("Enter the number of labs completed: "))
if labs_completed>6:
    labs_completed = 6
quizzes_completed = int(input("Enter the number of quizzes completed: "))
if quizzes_completed>6:
    quizzes_completed = 6
assignment1 = int(input("Enter grade for Assignment 1: "))
assignment2 = int(input("Enter grade for Assignment 2: "))
assignment3 = int(input("Enter grade for Assignment 3: "))
assignment4 = int(input("Enter grade for Assignment 4: "))
midterm1 = int(input("Enter grade for Midterm 1: "))
midterm2 = int(input("Enter grade for Midterm 2: "))
final = int(input("Enter grade for Final Exam: "))
preparation = int(input("Enter grade for Midterms and Final Preparation: "))
#doing the math
grade = labs_completed/6*20 + quizzes_completed/6*15 + (assignment1+assignment2+assignment3+assignment4)/400*16 + (midterm1+midterm2)/200*25 + final/100*18 + preparation/100*6
grade = round(grade)
grade = int(grade)
#printing
print("Your grade is:",grade)
