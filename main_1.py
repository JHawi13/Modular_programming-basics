import operators
import others
import trig

the_operator=input("enteroperator")

if the_operator=='+':
    num1=eval(input("Enter number 1:"))
    num2=eval(input("Enter number 2:"))
    operators.add(num1,num2)
elif the_operator=='-':
    num1=eval(input("Enter number 1:"))
    num2=eval(input("Enter number 2:"))
    operators.subtract(num1,num2)
elif the_operator=='X':
    num1=eval(input("Enter number 1:"))
    num2=eval(input("Enter number 2:"))
    operators.multiply(num1,num2)
elif the_operator=='/':
    num1=eval(input("Enter number 1:"))
    num2=eval(input("Enter number 2:")) 
    operators.divide(num1,num2)
elif the_operator=='cube':
    number=eval(input("Enter the number to be cubed"))
    others.cube(number)
elif the_operator=='sin':
    angle=eval(input("Enter the angle"))
    print(trig.get_sin(angle))
elif the_operator=='tan':
    angle=eval(input("Enter the angle"))
    print(trig.get_tan(angle))
elif the_operator=='cos':
    angle=eval(input("Enter the angle"))
    print(trig.get_cos(angle))
