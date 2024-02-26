#region Imports
import numpy as np
from scipy.linalg import solve
#endregion

#region Functions
def solve_matrix_equation(coeff_matrix, constant_vector):
    return solve(coeff_matrix, constant_vector)
#endregion

# First matrix equation
A1 = np.array([[3, 1, -1],
               [1, 4, 1],
               [2, 1, 2]])
b1 = np.array([2, 12, 10])

# Solve the first equation
x1 = solve_matrix_equation(A1, b1)

print("Solution to the first matrix equation:")
print("x1 =", x1[0])
print("x2 =", x1[1])
print("x3 =", x1[2])

# Second matrix equation
A2 = np.array([[1, -10, 2, 4],
               [3, 0, 12, 0],
               [9, 2, 3, 4],
               [0, 0, 7, 0]])
b2 = np.array([2, 12, 21, 37])

# Solve the second equation
x2 = solve_matrix_equation(A2, b2)

print("\nSolution to the second matrix equation:")
print("x1 =", x2[0])
print("x2 =", x2[1])
print("x3 =", x2[2])
print("x4 =", x2[3])
