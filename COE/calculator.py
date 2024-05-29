#addition function
def add(iNum1,iNum2):
    return iNum1+iNum2
#subtraction function
def subtract(iNum1,iNum2):
    return iNum1-iNum2
#multiplication function
def multiply(iNum1,iNum2):
    return iNum1*iNum2
#division function
def divide(iNum1,iNum2):
    return iNum1/iNum2
#taking input
iNum1=int(input("Enter first number:"))
iNum2=int(input("Enter the second number:"))
#enter the operation
print("Select the operation\n1.for addition\n2.for subtraction\n3.for Multiplication\n4.for Division")
iOperator=int(input("Enter the operator:"))
#conditions for operation
if iOperator==1:
    print(add(iNum1,iNum2))
elif iOperator==2:
    print(subtract(iNum1,iNum2))
elif iOperator==3:
    print(multiply(iNum1,iNum2))
elif iOperator==4:
    print(divide(iNum1,iNum2))
else:
    print("!!Wrong Input!!")