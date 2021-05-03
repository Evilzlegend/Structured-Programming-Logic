# Fahrenheit to Celsius formula -32*5/9

# Entering the input for the desired temperature conversion.
temperatureRequest=float(input("Please enter your degree temperature: "))

# Conversion formula for Fahrenheit to Celsius first part
temperatureFirst=temperatureRequest-32

# Conversion formula for Fahrenheit to Celsius second part
temperatureConversion=temperatureFirst*5/9

# Display outcome for conversion.
print("Your temperature from Fahrenheit to Celsius: ",(format(temperatureConversion,',.2f')))
