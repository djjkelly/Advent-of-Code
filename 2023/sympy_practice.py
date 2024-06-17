from sympy import symbols, Eq, solve

x = symbols('x')
y = symbols('y')

equation = Eq(x**3 - 4*x**2 + 13*x - 4, 42*y)
equations = [Eq(x**2, 9),Eq(x**3, -27), Eq(y, 3 * x**2)]
answer = solve(equations, (x,y))
print('answer:',answer)