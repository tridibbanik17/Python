"""
Convert a temperature from Fahrenheit to Celsius
"""
temp_farenhite = float(input("Temp in °F: "))

# Calculate it in Celsius
temp_celsius = (temp_farenhite - 32) * 5/9
# print("Temp in °C: " + str(round(temp_celsius, 2)))
# print("Temp in °C: {}".format(round(temp_celsius, 2)))
# print(f"Temp: {round(temp_celsius, 2)} °C")
unit = "C"
print(f"Temp: {round(temp_celsius, 2)} °{unit}")