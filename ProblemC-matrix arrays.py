#region Import
import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt
#endregion

#region Functions
def solve_matrix_equation(coeff_matrix, constant_vector):
    """
    Solves a system of linear equations represented by a coefficient matrix and a constant vector.

    Parameters:
        coeff_matrix (numpy.ndarray): Coefficient matrix of shape (n, n).
        constant_vector (numpy.ndarray): Constant vector of shape (n,).

    Returns:
        numpy.ndarray: Solution vector of shape (n,).

    Details:
        This function utilizes the `scipy.linalg.solve` function to find the solution vector 'x'
        for the linear system represented by the equation Ax = b, where A is the coefficient matrix
        and b is the constant vector. It directly solves the equation by computing the inverse of
        the coefficient matrix and then multiplying it with the constant vector.

        The `scipy.linalg.solve` function is chosen for its efficiency and accuracy in solving
        dense linear systems. It internally uses LAPACK routines to compute the solution,
        ensuring numerical stability and reliability.
    """
    return solve(coeff_matrix, constant_vector)
#endregio

# Define the coefficient matrix and constant vector for the first matrix equation
A1 = np.array([[3, 1, -1],
               [1, 4, 1],
               [2, 1, 2]])
b1 = np.array([2, 12, 10])

# Display the coefficient matrix A1
print("Coefficient matrix for the first equation (A1):")
print(A1)
print(b1)

# Solve the first equation
x1 = solve_matrix_equation(A1, b1)

# Define the coefficient matrix and constant vector for the second matrix equation
A2 = np.array([[1, -10, 2, 4],
               [3, 0, 12, 0],
               [9, 2, 3, 4],
               [0, 0, 7, 0]])
b2 = np.array([2, 12, 21, 37])

# Display the coefficient matrix A2
print("Coefficient matrix for the second equation (A2):")
print(A2)
print(b2)

# Solve the second equation
x2 = solve_matrix_equation(A2, b2)

# Plot solutions as tables
fig, axs = plt.subplots(2)

# Display solutions as tables
axs[0].axis('tight')
axs[0].axis('off')
axs[0].set_title('Solution to the first matrix equation')
table_data1 = [["x1", "x2", "x3"]] + [x1.tolist()]  # Prepare data for table display
axs[0].table(cellText=table_data1, loc='center')  # Display table with solution

axs[1].axis('tight')
axs[1].axis('off')
axs[1].set_title('Solution to the second matrix equation')
table_data2 = [["x1", "x2", "x3", "x4"]] + [x2.tolist()]  # Prepare data for table display
axs[1].table(cellText=table_data2, loc='center')  # Display table with solution

plt.show()  # Show the plots
