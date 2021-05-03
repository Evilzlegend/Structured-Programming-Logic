# Initialize variables
totalApartments = 0
totalOccupied = 0
floors = 0

# Get number of floors
numFloors = int(input("How many floors does the apartment have?"))

# Validate user entry
while numFloors < 1:
    numFloors = int(input("Invalid. Enter 1 or more: "))

# Count through floors and get the number of rooms occupied
for floor in range (1, numFloors + 1):
    apartments = int(input("How many apartments does floor "+ str(floor) +" have? "))
    # Validate the apartments are greater than 10
    while apartments < 10:
        apartments = int(input("Invalid. Enter 10 or more: "))
    # Calculate the total number of apartments
    totalApartments = totalApartments + apartments
    # Ask for number occupied
    occupied = int(input("How many occupied apartments does floor "+ str(floor) +" have? "))
    totalOccupied = totalOccupied + occupied

# Perform occupancy calculations
occupancyRate = totalOccupied / totalApartments * 100
vacant = totalApartments - totalOccupied

# Print output
print("Number of apartments:", totalApartments)
print("Occupied apartments: ", totalOccupied)
print("Vaccant apartments: ", vacant)
print("Occupancy rate: ",format( occupancyRate,",.2f"), "%")