# Formula: 703 x weight (lbs) / [height (in)]2
# When using English measurements, pounds should be divided by inches squared.
# This should then be multiplied by 703 to convert from lbs/inches2 to kg/m2.

# Entering Height
height=float(input("What is your height in inches? "))

# Entering Weight
weight=float(input("What is your weight in pounds? "))

# Formula for BMI conversion
bmi=703*weight/height**2

# This will show BMI total
print("Your BMI is:",(format(bmi,'.2f')))
