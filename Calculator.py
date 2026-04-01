
def calculator(numberOne, numberTwo, operation):
    if operation == "+":
        solved = numberOne + numberTwo
        
    elif operation == "-":
        solved = numberOne - numberTwo
       
    elif operation == "/":
        solved = numberOne / numberTwo
        
    elif operation == "*":
        solved = numberOne * numberTwo

    else:
        print("Wrong operator")
        
    print(solved)
    return(solved)      


    


