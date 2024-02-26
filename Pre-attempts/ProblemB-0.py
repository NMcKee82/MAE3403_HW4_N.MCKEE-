import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


def equation1(x):
    return x - 3 * np.cos(x)


def equation2(x):
    return np.cos(2 * x) * x ** 3


def find_intersections():
    """
    Find all intersection points of the two equations.

    Returns:
        array_like: The x-coordinate(s) of the intersection point(s).
    """
    # Define a function that computes the difference between the two equations
    intersection_function = lambda x: equation1(x) - equation2(x)

    # Define the range of x values to search for intersections
    x_values = np.linspace(-5, 5, 1000)

    # Initialize list to store intersection points
    intersection_points = []

    # Iterate over the range of x values and find intersections
    for i in range(len(x_values) - 1):
        x1, x2 = x_values[i], x_values[i + 1]
        root = fsolve(intersection_function, [x1])  # Use the lower bound of the interval as the initial guess
        for r in root:
            if -5 <= r <= 5:  # Filter out intersection points outside the plotted range
                # Check if the absolute difference between the function values is close to zero
                if np.abs(equation1(r) - equation2(r)) < 0.01:  # Adjust the tolerance as needed
                    intersection_points.append(r)

    # Remove duplicate intersection points
    intersection_points = list(set(intersection_points))

    return intersection_points


# Find the roots of equation 1
roots1 = fsolve(equation1, [0, 1, 2, 3, 4])

# Find the roots of equation 2
roots2 = fsolve(equation2, [-1, 0, 1, 2, 3])


# Plot the equations and mark all intersections
def plot_equations_with_intersections():
    """
    Plot both equations and add white circles with red borders at all intersection points and text displaying the xy coordinates of the intersections.
    """
    # Generate x values for plotting
    x_values = np.linspace(-5, 5, 400)

    # Plot the equations
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, equation1(x_values), label='x - 3*cos(x)')
    plt.plot(x_values, equation2(x_values), label='cos(2*x)*x^3')

    # Find and plot all intersection points
    intersection_points = find_intersections()
    for intersection_point in intersection_points:
        plt.plot(intersection_point, equation1(intersection_point), 'wo', markersize=10,
                 markeredgecolor='r')  # white circle with red border
        plt.text(intersection_point, equation1(intersection_point) + 0.5,
                 f'({intersection_point:.2f}, {equation1(intersection_point):.2f})', color='black')

    # Add labels, title, legend, and grid
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Intersection of Two Equations')
    plt.legend()
    plt.grid(True)

    # Show plot
    plt.show()


# Print roots and intersection points
print("Roots of equation 1:", roots1)
print("Roots of equation 2:", roots2)
print("Intersection points:", find_intersections())

# Plot equations with intersections
plot_equations_with_intersections()
