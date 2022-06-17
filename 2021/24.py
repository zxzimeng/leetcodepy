import itertools
numbers = []
num1 = input("Enter First number: ")
num2 = input("Enter Second number: ")
num3 = input("Enter Third number: ")
num4 = input("Enter Fourth number: ")
numbers.append(num1)
numbers.append(num2)
numbers.append(num3)
numbers.append(num4)
number_list = list(itertools.permutations(numbers))
has_answer = False
for numbers in number_list:
    operators = ['+', '*', '-', '/']
    for operator1 in operators:
        result1 = eval(numbers[0] + operator1 + numbers[1])
        for operator2 in operators:
            result2 = eval(str(result1) + operator2 + numbers[2])
            for operator3 in operators:
                problem = eval(str(result2) + operator3 + numbers[3])
                if problem == 24.000:
                    print("(("+ numbers[0] + operator1 +numbers[1] +")"+ operator2  +numbers[2] +")"+ operator3 +numbers[3], "=", problem)
                    has_answer = True
if not has_answer:
    print("impossible")
