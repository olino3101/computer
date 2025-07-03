from utils import format_decimal

def resolve_linear_equation(equation):
    solution = equation[0] / -equation[1]
    solution = format_decimal(solution)
    print("The solution is:" \
    f"{solution}")