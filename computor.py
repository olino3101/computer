import numpy as np
import re
from typing import Optional, Tuple
from parsing import check_arg, get_coefficients
from utils import get_right_notation
from quadratic import resolve_quadratic
from linear import resolve_linear_equation
from utils import trim_zero

def find_degree(equation):
    exponents = re.findall(r'X\^(\d+)', equation)
    if not exponents:
        return 0
    degrees = list(map(int, exponents))
    return max(degrees)

def get_reduced_form(left, right) -> Optional[Tuple[np.ndarray, np.ndarray]]:
    # sometimes the right side as more coefficients than the left side
    for i in range(len(right)):
        if i >= len(left):
            left = np.append(left, -right[i])
        else:
            left[i] -= right[i]
        right[i] -= right[i]
    left, right = trim_zero(left, right)
    print(f"Left side after reduction: {left}, Right side after reduction: {right}")
    return left, right

# Positive discriminant (b² - 4ac > 0): Two distinct real roots.
# Zero discriminant (b² - 4ac = 0): One real root (a repeated root).
# Negative discriminant (b² - 4ac < 0): Two complex conjugate roots
def resolve_equation(equation, degree, is_same):
    match degree:
        case 0 if is_same:
            print("Any real number is a solution.")
        case 0:
            print("No solution.")
        case 1:
            resolve_linear_equation(equation)
        case 2:
            resolve_quadratic(equation) 
        case _:
            print("The polynomial degree is strictly greater than 2, I can't solve.")

def main():
    # print(f"left {coefficients_left}, right {coefficients_right}, indvi {tokens}")
    try:
        equation_text = check_arg()
        
        left, right  = get_coefficients(equation_text)
        print(f"Left side: {left}, Right side: {right}")
        # reduced form
        left_RF, right_RF = get_reduced_form(left, right)
        # check if they are same
        is_same = np.array_equal(left_RF, right_RF)
        reduced_form_notation = get_right_notation(left_RF, right_RF, True)
        print(f"Reduce form: {reduced_form_notation}")
        degree = find_degree(reduced_form_notation)
        if degree != 0:
            print(f"Polynomial degree: {degree}")
        resolve_equation(left_RF ,degree, is_same)
    except ValueError as e:
        print(f"{e}")
    except TypeError as e:
        print(f"{e}")
    except Exception as e:
        print(f"{e}")


if __name__ == "__main__":
    main()
