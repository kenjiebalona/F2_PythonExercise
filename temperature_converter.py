def celsius_to_fahrenheit(celsius):
  fahrenheit = (celsius * 9/5) + 32
  return round(fahrenheit, 2)

celsius = float(input("Please enter a temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print("Equivalent temperature in Fahrenheit: ", fahrenheit)