NUM_DAYS = 5

# Create a list to hold the sales
# for each day.
sales = [0] * NUM_DAYS
print(sales)
# Create a variable to hold an index.
index = 0

print('Enter the sales for each day.')

# Get the sales for each day.
while index < NUM_DAYS:
    print('Day #', index + 1, ': ', sep='', end='')
    sales[index] = int(input())
    index += 1
    
# Display the values entered.
print('Here are the values you entered:')
for value in sales:
    print(value)
