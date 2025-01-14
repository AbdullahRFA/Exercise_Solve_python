"""

create a calculator capable of performing additions, subtraction, multiplication,
and division operation on two numbers.

your program should output in readable manner

program should terminate when user press q

"""
while True:
    num1 = input("Enter first number : ")
    if num1 =='q':
        break
    num2 = input("Enter second number : ")
    if  num2 == 'q':
        break
    num1 = int(num1)
    num2 = int(num2)
    print(f"Sum of {num1} + {num2} : ",num1+num2)
    print(f"Sub of {num1} - {num2} : ",num1-num2)
    print(f"Mul of {num1} * {num2} : ",num1*num2)
    print(f"Div of {num1} / {num2} : ",num1/num2)


