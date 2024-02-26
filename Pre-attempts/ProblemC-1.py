import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt

def solve_matrix_equation(coeff_matrix, constant_vector):
    return solve(coeff_matrix, constant_vector)

# First matrix equation
A1 = np.array([[3, 1, -1],
               [1, 4, 1],
               [2, 1, 2]])
b1 = np.array([2, 12, 10])

# Solve the first equation
x1 = solve_matrix_equation(A1, b1)

# Second matrix equation
A2 = np.array([[1, -10, 2, 4],
               [3, 0, 12, 0],
               [9, 2, 3, 4],
               [0, 0, 7, 0]])
b2 = np.array([2, 12, 21, 37])

# Solve the second equation
x2 = solve_matrix_equation(A2, b2)

# Plot solutions as tables
fig, axs = plt.subplots(2)

# First table
axs[0].axis('tight')
axs[0].axis('off')
axs[0].set_title('Solution to the first matrix equation')
table_data1 = [["x1", "x2", "x3"]] + [x1.tolist()]
axs[0].table(cellText=table_data1, loc='center')

# Second table
axs[1].axis('tight')
axs[1].axis('off')
axs[1].set_title('Solution to the second matrix equation')
table_data2 = [["x1", "x2", "x3", "x4"]] + [x2.tolist()]
axs[1].table(cellText=table_data2, loc='center')

plt.show()
