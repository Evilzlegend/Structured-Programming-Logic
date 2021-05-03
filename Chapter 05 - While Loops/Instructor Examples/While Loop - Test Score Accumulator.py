# This program averages test scores. It asks the user for the
# number of students and the number of test scores per student.

# Get the number of students.
numStudents = int(input("How many students do you have? "))

# Get the number of test scores per student.
numTestScores = int(input("How many test scores per student? "))

# Determine each students average test score.
for student in range(numStudents):
    # Initialize an accumulator for test scores.
    total = 00.0
    # Get a student's test scores.
    print("Student number", student+1)
    print("--------------")

    for testNum in range(numTestScores):
        print("Test number", testNum +1, end="")
        score = float(input(": "))
        #Add the score to the accumulator
        total += score

    # Calculate the average test score for this student.
    average = total/numTestScores

    #Display the average.
    print("The average for student number", student+1, \
          "is:", format(average, ".2f"))
    print()
