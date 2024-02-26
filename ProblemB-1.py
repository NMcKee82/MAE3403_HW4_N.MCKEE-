#region Import
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
#endregion

#region Functions
def equation1(x):
    """
    Calculate the value of the first equation, which is defined as x - 3 * cos(x).

    This equation represents a simple algebraic expression where x is subtracted by
    the product of 3 and the cosine of x. The cosine function, denoted as cos(x),
    calculates the cosine value of the angle x in radians. The result of this equation
    signifies a relationship between a linear term (x) and a periodic term (cos(x)),
    providing insight into their intersection points.

    Parameters:
        x (float or array_like): The input value(s) for which to evaluate the equation.

    Returns:
        float or array_like: The result(s) of the equation evaluation.
    """
    return x - 3 * np.cos(x)


def equation2(x):
    """
    Compute the value of the second equation, given by cos(2 * x) * x**3.

    This equation involves two mathematical operations: cosine function (cos(x)) and
    exponentiation (x**3). The cosine function calculates the cosine value of the
    angle 2*x, where x is the input value. The result is then multiplied by the
    cube of x. The equation represents a combination of trigonometric and algebraic
    functions, exhibiting both periodic and polynomial behavior.

    Parameters:
        x (float or array_like): The input value(s) for which to compute the equation.

    Returns:
        float or array_like: The computed value(s) of the equation.
    """
    return np.cos(2 * x) * x ** 3


def find_intersections():
    """
    Determine all intersection points of the two equations using numerical methods.

    This function utilizes the concept of root-finding to locate the points where
    the two equations intersect. It defines an intersection function as the
    difference between equation1(x) and equation2(x). By iterating over a range
    of x values and applying a root-finding algorithm (in this case, fsolve),
    it identifies the x-coordinates of the intersection points. The function
    then filters out any extraneous points and eliminates duplicates to provide
    a clean list of intersection coordinates.

    Returns:
        array_like: An array containing the x-coordinates of all intersection points.
    """
    intersection_function = lambda x: equation1(x) - equation2(x)
    x_values = np.linspace(-5, 5, 1000)
    intersection_points = []
    for i in range(len(x_values) - 1):
        x1, x2 = x_values[i], x_values[i + 1]
        root = fsolve(intersection_function, [x1])
        for r in root:
            if -5 <= r <= 5:
                if np.abs(equation1(r) - equation2(r)) < 0.01:
                    intersection_points.append(r)
    intersection_points = list(set(intersection_points))
    return intersection_points


def plot_equations_with_intersections():
    """
    Plot both equations and mark their intersection points for visualization.

    This function generates a plot that illustrates the behavior of the two equations
    over a specified range of x values. It utilizes matplotlib to create the plot,
    with separate lines for each equation. Intersection points are identified using
    find_intersections() function and marked on the plot as white circles with red
    borders. Additionally, text annotations are added near each intersection point
    to display their coordinates. The plot is adorned with axis labels, a title,
    a legend, and gridlines to enhance clarity.
    """
    x_values = np.linspace(-5, 5, 400)
    plt.figure(figsize=(8, 6))
    plt.plot(x_values, equation1(x_values), label='x - 3*cos(x)')
    plt.plot(x_values, equation2(x_values), label='cos(2*x)*x^3')
    intersection_points = find_intersections()
    for intersection_point in intersection_points:
        plt.plot(intersection_point, equation1(intersection_point), 'wo', markersize=10, markeredgecolor='r')
        plt.text(intersection_point, equation1(intersection_point) + 0.5,
                 f'({intersection_point:.2f}, {equation1(intersection_point):.2f})', color='black')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Intersection of Two Equations')
    plt.legend()
    plt.grid(True)
    plt.show()
#endregions

# Find the roots of equation 1
roots1 = fsolve(equation1, [0, 1, 2, 3, 4])

# Find the roots of equation 2
roots2 = fsolve(equation2, [-1, 0, 1, 2, 3])

# Print roots and intersection points
print("Roots of equation 1:", roots1)
print("Roots of equation 2:", roots2)
print("Intersection points:", find_intersections())

# Plot equations with intersections
plot_equations_with_intersections()
