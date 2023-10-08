temp_scale = (input("What type of temperatue you want to choose Celsius(C) or Fahrenheit(F) "))
temp = (float(input("Enter your temperature ")))

if (temp_scale == "C"):
    converted_temp = (temp - 32)/ 1.8
    print("Temperatur in Celsius: {:.2f}°C".format(converted_temp))
elif (temp_scale == "F"):
    converted_temp = (temp * 1.8)/ 5 + 32
    print ("Temperatur in Fahrenheit: {:.2f}°F".format(converted_temp))
else:
    print("You write wrong values pls choose C of F")