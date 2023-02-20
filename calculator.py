#Lets go
def any_simple_calculation (Equation):
    for i in range(len(Equation)):
        if Equation[i]=='/':
            operator=Equation.index('/')
            num1=int(Equation[0:operator])
            num2=int(Equation[operator+1:])
            return print(num1/num2)
        elif Equation[i]=='X':
            operator=Equation.index('X')
            num1=int(Equation[0:operator])
            num2=int(Equation[operator+1:])
            return print(num1*num2)
        elif Equation[i]=='x':
            operator=Equation.index('x')
            num1=int(Equation[0:operator])
            num2=int(Equation[operator+1:])
            return print(num1*num2)
        elif Equation[i]=='*':
            operator=Equation.index('*')
            num1=int(Equation[0:operator])
            num2=int(Equation[operator+1:])
            return print(num1*num2)
        elif Equation[i]=='+':
            operator=Equation.index('+')
            num1=int(Equation[0:operator])
            num2=int(Equation[operator+1:])
            return print(num1+num2)
        elif Equation[i]=='-':
            operator=Equation.index('-')
            num1=int(Equation[0:operator])
            num2=int(Equation[operator+1:])
            return print(num1-num2)
def complex_calculations(equation):
    operatorpositions=[]
    for i in equation:
        if i=='+':
            plus_position=equation.index('+')
            operatorpositions.append(plus_position)
        if i=='-':
            minus_position=equation.index('-')
            operatorpositions.append(minus_position)
        if i=='/':
            divide_position=equation.index('/')
            operatorpositions.append(divide_position)
        if i=='x'or i=='X' or i=='*':
            multiply_position=equation.index(i)
            operatorpositions.append(multiply_position)
    operatorpositions.sort()
    if equation.count('x')>0 or equation.count('X')>0 or equation.count('*'):
        if multiply_position == operatorpositions[0] :
            if len(operatorpositions)>1:
                nextoperator=operatorpositions[1]
                isolated_equation=equation[0:nextoperator]
                result_of_isolated_equation=any_simple_calculation(isolated_equation)
                remaining_equation=equation.replace(equation[0:nextoperator],str(result_of_isolated_equation))
                complex_calculations(remaining_equation)
            else:
                return print(any_simple_calculation(equation))
        elif multiply_position==int:
            previous_operator=operatorpositions[operatorpositions.index(multiply_position)-1]
            if operatorpositions[operatorpositions.index(multiply_position)+1]==int:
                next_operator=operatorpositions[operatorpositions.index(multiply_position)+1]
                isolated_equation=equation[previous_operator+1:next_operator]
                result_of_isolated_equation=any_simple_calculation(isolated_equation)
                remaining_equation=equation.replace(equation[previous_operator+1:nextoperator,str(result_of_isolated_equation)])
            else:
                isolated_equation=equation[previous_operator+1:]
                result_of_isolated_equation=any_simple_calculation(isolated_equation)
    #End of multipliation part
    if equation.count('/')>0 :
        if divide_position == operatorpositions[0] :
            if len(operatorpositions)>1:
                nextoperator=operatorpositions[1]
                isolated_equation=equation[0:nextoperator]
                result_of_isolated_equation=any_simple_calculation(isolated_equation)
                remaining_equation=equation.replace(equation[0:nextoperator],str(result_of_isolated_equation))
                complex_calculations(remaining_equation)
            else:
                return print(any_simple_calculation(equation))
        elif divide_position==int:
            previous_operator=operatorpositions[operatorpositions.index(divide_position)-1]
            if operatorpositions[operatorpositions.index(divide_position)+1]==int:
                next_operator=operatorpositions[operatorpositions.index(divide_position)+1]
                isolated_equation=equation[previous_operator+1:next_operator]
                result_of_isolated_equation=any_simple_calculation(isolated_equation)
                remaining_equation=equation.replace(equation[previous_operator+1:nextoperator,str(result_of_isolated_equation)])
            else:
                isolated_equation=equation[previous_operator+1:]
                result_of_isolated_equation=any_simple_calculation(isolated_equation)
    #End of division part
    if equation.count('+')>0:
        if plus_position == operatorpositions[0] :
            if len(operatorpositions)>1:
                nextoperator=operatorpositions[1]
                isolated_equation=equation[0:nextoperator]
                result_of_isolated_equation=any_simple_calculation(isolated_equation)
                remaining_equation=equation.replace(equation[0:nextoperator],str(result_of_isolated_equation))
                complex_calculations(remaining_equation)
            else:
                return print(any_simple_calculation(equation))
        elif plus_position==int:
            previous_operator=operatorpositions[operatorpositions.index(plus_position)-1]
            if operatorpositions[operatorpositions.index(plus_position)+1]==int:
                next_operator=operatorpositions[operatorpositions.index(plus_position)+1]
                isolated_equation=equation[previous_operator+1:next_operator]
                result_of_isolated_equation=any_simple_calculation(isolated_equation)
                remaining_equation=equation.replace(equation[previous_operator+1:nextoperator,str(result_of_isolated_equation)])
            else:
                isolated_equation=equation[previous_operator+1:]
                result_of_isolated_equation=any_simple_calculation(isolated_equation)
    #End of addition part
    if equation.count('-')>0:
        if minus_position == operatorpositions[0] :
            if len(operatorpositions)>1:
                nextoperator=operatorpositions[1]
                isolated_equation=equation[0:nextoperator]
                result_of_isolated_equation=any_simple_calculation(isolated_equation)
                remaining_equation=equation.replace(equation[0:nextoperator],str(result_of_isolated_equation))
                complex_calculations(remaining_equation)
            else:
                return print(any_simple_calculation(equation))
        elif minus_position==int:
            previous_operator=operatorpositions[operatorpositions.index(minus_position)-1]
            if operatorpositions[operatorpositions.index(minus_position)+1]==int:
                next_operator=operatorpositions[operatorpositions.index(minus_position)+1]
                isolated_equation=equation[previous_operator+1:next_operator]
                result_of_isolated_equation=any_simple_calculation(isolated_equation)
                remaining_equation=equation.replace(equation[previous_operator+1:nextoperator,str(result_of_isolated_equation)])
            else:
                isolated_equation=equation[previous_operator+1:]
                result_of_isolated_equation=any_simple_calculation(isolated_equation)
    #End of minus part
problem=input("Enter the equation:")
complex_calculations(problem)
def separate_parts_of_an_equation(equation):
    