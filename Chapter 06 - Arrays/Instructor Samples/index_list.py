# This program demonstrates how to get the
# index of an item in a list and then replace
# that item with a new item.

# Create a list with some items.
food = ['Pizza', 'Burgers', 'Chips']

# Display the list.
print('Here are the items in the food list:')
print(food)

# Get the item to change.
item = input('Which item should I change? ')

# Get the item's index in the list.
itemIndex = food.index(item)
print(itemIndex)

# Get the value to replace it with.
newItem = input('Enter the new value: ')

# Replace the old item with the new item.
food[itemIndex] = newItem

# Display the list.
print('Here is the revised list:')
print(food)