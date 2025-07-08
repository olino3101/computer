from typing import Optional, Tuple
import numpy as np

def format_decimal(nbr):
    if isinstance(nbr, float) and nbr.is_integer():
        return str(int(nbr))
    else:
        return str(nbr)

def transform_coefficients_to_notation(arr):
    notation = ' '.join(
        ((("-" if x < 0 else " ") if i == 0 
          else (" - " if x < 0 else " + ")) 
         + str(format_decimal(abs(x))) + f" * X^{i}")
        for i, x in enumerate(arr))
    return notation

# use the get the right notation the same way as you receive it
def get_right_notation(left, right, is_RF):
    left_notation = transform_coefficients_to_notation(left)
    right_notation = transform_coefficients_to_notation(right)
    if is_RF:
        right_notation = "0"
    result = left_notation + " = " + right_notation
    return result

def trim_zero(l, r) -> Optional[Tuple[np.ndarray, np.ndarray]]:
    i = 1
    while i <= len(l):
        if l[-i] == 0 and len(r) <= i and len(l) > 1:
            l = np.delete(l, -i)
        elif l[-i] == 0 and len(r) > i and r[-i] == 0:
                l = np.delete(l, -i)
                r = np.delete(r, -i)
        else:
            break
    return l, r
