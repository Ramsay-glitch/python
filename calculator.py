print("Calculator application\n")
print("addition +\n")
print("subtraction -\n")
print("Multipulication *\n")
print("divition /\n")
print("Floor divition //\n")
print("Module %\n")
try:
    a = float(input("enter the first number:"))
    op = input("enter the operator:")
    b = float(input("enter the second number:"))
    if op=='+':
        print("addition:",a+b,'\n')
    elif op=="-":
        print("Subtration:",a-b,'\n')
    elif op=="*":
        print("Multipulication:",a*b,'\n')
    elif op=="/":
        print("Divition:",a/b,"\n")
    elif op=="//":
        print("Floor Divitionn:",a//b,"\n")
    elif op=="%":
        print("Module:",a%b,"\n")
    else:
        print("operator error")
except ValueError:
    print("only number accepted")
