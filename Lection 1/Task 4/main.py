cmd = "math_calculation"
math_calculation=(input("which operation do you want? Plus(+) , Minus(-) , Division(/) , Multiplication(*) , Root(√) or Exponentiation(**)" ))
a=(int(input("Number 1: ")))
b=(int(input("Number 2: ")))

match math_calculation:
    case "+":
        print("c = " , a + b)
    case "-":
        print("c = " , a - b)
    case "*":
        print("c = " , a * b)
    case "/":
        if b != 0:
            print("c = " , a / b)
        else:
            print("Error!!!!")
    case "**":
        print("c = " , a ** b)
    case "√":                               #To get this mathematical sign use Alt + 251
        print("c = " , a ** 0.5 )
    case _:
        print("This is not operation try again")
        
print("c = " , math_calculation)