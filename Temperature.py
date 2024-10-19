class Temperature:
    
    def convertFahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit}°F")
        return fahrenheit

   
    def convertCelsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius}°C")
        return celsius


temp = Temperature()


print("Temperature Conversion:")
print("1. Convert Celsius to Fahrenheit")
print("2. Convert Fahrenheit to Celsius")
choice = int(input("Choose an option (1 or 2): "))

if choice == 1:
    
    celsius = float(input("Enter temperature in Celsius: "))
    temp.convertFahrenheit(celsius)
elif choice == 2:
    
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    temp.convertCelsius(fahrenheit)
else:
    print("Invalid choice!")
    
