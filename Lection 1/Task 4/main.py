cmd = "math_calculation"
math_calculation=(input("which operation do you want? Plus(+) , Minus(-) , Division(/) , Multiplication(*) , Root(√) or Exponentiation(**)" ))
Number_1=(int(input( )))       
Number_2=(int(input( )))        

result = None

match math_calculation:
    case "+":
        print("res = " , Number_1 + Number_2)      
    case "-":
        print("res = " , Number_1 - Number_2)
    case "*":
        print("res = " , Number_1 * Number_2)
    case "/":
        if Number_2 != 0:
            print("res = " , Number_1 / Number_2)
        else:
            print("Error!!!!")
    case "**":
        print("res = " , Number_1 ** Number_2)
    case "√":                                                   #To get this mathematical sign use Alt + 251
        print("res = " , Number_1 ** 0.5 )
    case _:
        print("This is not operation try again")
if result is not None:
    print("Result:" , math_calculation)