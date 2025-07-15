import math
from utils import format_decimal

def get_discriminant(equation):
    discriminant = equation[1] ** 2 - (4 * equation[0] * equation[2])
    return discriminant

def GCD(last, remainder):
    if remainder == 0:
        raise ZeroDivisionError()
    while last % remainder != 0:
        remainder = last % remainder
    return remainder

def euclidean_algo(b, div_a, i_nbr):
    arr = [b, div_a, i_nbr]
    arr.sort()

    remainder = GCD(arr[2], arr[1])
    remainder = GCD(arr[0], remainder)
    return remainder

def pos_discriminant(equation, discriminant):
    sqrt_discriminant = math.sqrt(discriminant)
    div_a = (2 * equation[2])
    first_solution = (-equation[1] + sqrt_discriminant) / div_a
    second_solution = (-equation[1] - sqrt_discriminant) / div_a
    
    first_solution = round(first_solution, 5)
    second_solution = round(second_solution, 5)

    print("Discriminant is strictly positive, the two solutions are:\n" \
    f"{first_solution}\n{second_solution}")

def neg_discriminant_has_zero(div_a, i_nbr):
    gcd = GCD(div_a, i_nbr)
    if gcd % 1 == 0:
        i_nbr, div_a = i_nbr/gcd, div_a/gcd
    
    div_a = round(div_a, 5)
    i_nbr = round(i_nbr, 5)
    
    formatted_div_a = format_decimal(div_a)
    imag_part = format_decimal(i_nbr)
    first_solution = f"{imag_part}i/{formatted_div_a}"
    second_solution = f"-{imag_part}i/{formatted_div_a}"
    print("Discriminant is strictly negative, the two complex solutions are:\n" \
    f"{first_solution}\n{second_solution}")


def neg_discriminant(equation, discriminant):
    #transform discriminant into i number -4 = 2i because first i is -1 and 4
    div_a = (2 * equation[2])
    i_nbr = math.sqrt(abs(discriminant))
    if equation[1] == 0:
        neg_discriminant_has_zero(div_a, i_nbr)
        return 
    #simplifies everything
    gcd = euclidean_algo(-equation[1], div_a, i_nbr)
    if gcd % 1 == 0:
        equation[1], i_nbr, div_a = equation[1]/gcd, i_nbr/gcd, div_a/gcd

    # solution in string and rounded everything
    formatted_div_a = format_decimal(round(div_a, 5))
    real_part = format_decimal(round(-equation[1], 5))
    imag_part = format_decimal(round(i_nbr, 5))
    first_solution = f"{real_part}/{formatted_div_a} + {imag_part}i/{formatted_div_a}"
    second_solution = f"{real_part}/{formatted_div_a} - {imag_part}i/{formatted_div_a}"
    print("Discriminant is strictly negative, the two complex solutions are:\n" \
    f"{first_solution}\n{second_solution}")
        

# x = -b / 2a
def zero_discriminant(equation):
    div_a = (2 * equation[2])
    solution = -equation[1] / div_a
    print("Discriminant is zero, the only solutions is:\n" \
    f"{solution}")

# x = (-b ± √(b² - 4ac)) / 2a
# a = equation[2]
# b = equation[1]
# c = equation[0]
def resolve_quadratic(equation):
    discriminant = round(get_discriminant(equation), 2)
    if discriminant > 0:
        pos_discriminant(equation, discriminant)
    elif discriminant < 0:
        neg_discriminant(equation, discriminant)
    else:
        zero_discriminant(equation)
