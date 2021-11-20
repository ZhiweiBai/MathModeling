import numpy as np
from scipy.optimize import linprog
z1 = np.array([-100, -90, -80, -70])
z2 = np.array([0, 3, 0, 2])
A = np.matrix([[-1,0,3,0], [-1,0,0,3], [0,-1,2,0], [0,-1,0,2]]).T
b = np.matrix([-30, -30, 120, 48]).T
resp1 = linprog(z1, A_ub=A, b_ub=b, method="simplex")
resp2 = linprog(z2, A_ub=A, b_ub=b, method="simplex")
print(f"z1:\n{resp1}\n z2:\n{resp2}")
