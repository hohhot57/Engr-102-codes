
from sympy_old import *
import numpy as np

KnownVar = 5
x = symbols('x')
y = symbols('y')
eq1 = Eq(5*x + 5*y - 7, 0)
eq2 = Eq(6*x - 4*y - 9, 0)
solution = solve((eq1,eq2),x,y)
print(solution)
x = solution[x]
print(N(x))
print(np.sin())