list1 = [1, 2, 3, 4]
list2 = list1
print(list1)
print(list2)
print()
print()
list1[0] = 99
print(list1)
print(list2)

# Create a list with values.
list1 = [1, 2, 3, 4]
print(list1)
# Create an empty list.
list2 = []
# Copy the elements of list1 to list2
for item in list1:
    list2.append(item)
list1[0] = 99
print(list1)
print(list2)
