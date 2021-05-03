x=25
y=15
z=25

# range checking using AND
if x>=20 and x<=40:
    print("The value is in the acceptable range.")

# range checking using OR
if y<20 or y>40:
    print("The value is outside the acceptable range.")

#Don't do this
    if z<20 and z>40:
        print("The value is inside the acceptable range.")
