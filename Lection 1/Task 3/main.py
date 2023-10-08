temp_scale = (input("What type of temperatue you want to choose Celsius(C) or Fahrenheit(F)"))
temp = (float(input("Enter your temperature")))

if (temp_scale=="C"):
    temp = (temp - 32)/ 1.8
    print("convert value" , temp)
elif (temp_scale=="F"):
    temp = (temp * 1.8)/ 5 + 32
    print ("covert value" , temp)
else:
    print("You write wrong values")