from sympy import symbols, Eq, solve

x = symbols('x')
y = symbols('y')

equation = Eq(x**3 - 4*x**2 + 13*x - 4, 42*y)
answer = solve([equation], x)
print('answer:',answer)