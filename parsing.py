import sys
from typing import Optional, Tuple
import numpy as np
from utils import trim_zero

def check_arg():
    if len(sys.argv) != 2:
        raise TypeError("Wrong number of arguments. Needs one")
    return sys.argv[1]

def parse_side(tokens):
    nbr_to_append = float(tokens[1])
    if tokens[0] == "-":
        nbr_to_append *= -1
    del tokens[:4]
    return nbr_to_append

def get_coefficients(equation_text) -> Optional[Tuple[np.ndarray, np.ndarray]]:
    tokens = equation_text.split(" ")
    
    coefficients_left = [float(tokens[0])]
    # x * x^1 delete all that
    del tokens[:3]
    while tokens[0] != "=":
        coefficients_left.append(parse_side(tokens))

    # del the =
    del tokens[0]

    coefficients_right = [float(tokens[0])]
    # x * x^1 delete all that
    del tokens[:3]
    while len(tokens) > 0:
        coefficients_right.append(parse_side(tokens))

    # remove number that equals to 0
    coefficients_left, coefficients_right = trim_zero(coefficients_left, coefficients_right)
    if len(coefficients_left) == 0:
        raise Exception("Equation is only 0")
    return np.array(coefficients_left), np.array(coefficients_right)
