# Computor v1

This is a Python program that parses and solves polynomial equations of degree 2 or lower. It reduces the equation, identifies its degree, and computes real or complex solutions depending on the discriminant.

## 🚀 How to Run

Make sure you have Python 3 installed, then run:

  python computor.py "your equation here"

### Example:

  python computor.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"

Output:
  Reduced form: 4 * X^0 + 4 * X^1 - 9.3 * X^2 = 0  
  Polynomial degree: 2  
  Discriminant is strictly positive, the two solutions are:  
  0.905239  
  -0.475131  

## ✏️ Equation Format

- Each term must follow the format: `coefficient * X^exponent`
- Use `+` or `-` between terms
- Exponents must be integers (e.g. X^0, X^1, X^2)
- Both sides of the equation must be separated by `=`

Example of valid input:

  "1 * X^0 + 2 * X^1 + 3 * X^2 = 0"

## ✅ What It Does

- Parses and simplifies both sides of the equation
- Displays the reduced form
- Shows the polynomial degree
- Solves for:
  - One real root (discriminant = 0)
  - Two real roots (discriminant > 0)
  - Two complex roots (discriminant < 0)

This project was built to refresh core math skills through coding. It is part of a series of foundational tools used in more advanced subjects.
