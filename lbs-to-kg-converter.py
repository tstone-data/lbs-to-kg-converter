
# Welcome the user
print('Welcome to the pound-to-kilogram converter!')

# Take the user input
weight_pounds = input('What is the weight you want to convert? \nPlease enter here: ')

# Converting string to float
weight_pounds = float(weight_pounds)

# Executing the conversion formula
weight_kilograms = weight_pounds * .453592

# Returning the converted value to user
print(f'{weight_pounds:.2f} lbs is {weight_kilograms:.2f} kg')
