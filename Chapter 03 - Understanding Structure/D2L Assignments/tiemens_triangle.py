#Obtain the user's Triangle A input.
triAB = float(input("What is the base of Triangle A? "))
triAH = float(input("What is the height of Triangle A? "))
#Print the area of Triangle A.
triAA = triAB*triAH/2
print("The area of Triangle A is, ", (format(triAA, '.2f')))


#Obtain the user's Triangle B input.
triBB = float(input("What is the base of Triangle B? "))
triBH = float(input("What is the height of Triangle B? "))
#Print the area of Triangle B.
triBA = triBB*triBH/2
print("The area of Triangle B is, ", (format(triBA, '.2f')))

#Explain which Triangle has more area or the same area.
if triAA > triBA:
    print("Triangle A has the greater area than Triangle B.")

elif triAA < triBA:
    print("Triangle B has the greater area than Triangle A.")

elif triAA == triBA:
    print("Both Triangles have the same area.")
