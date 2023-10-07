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
        print("c = " , a / b)
    case "**":
        print("c = " , a ** b)
    case "√":
        print("c = " , a ** 0.5 )
        
print("c = " , math_calculation)