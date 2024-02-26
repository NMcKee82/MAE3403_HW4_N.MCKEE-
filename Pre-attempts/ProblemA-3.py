import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from scipy import stats

def generate_data():
    """
    Generate data for two normal distributions.

    This function generates data for two normal distributions, representing Equation 1 and Equation 2.
    Equation 1 represents a standard normal distribution with mean (μ) = 0 and standard deviation (σ) = 1.
    Equation 2 represents a normal distribution with mean (μ) = 175 and standard deviation (σ) = 3.

    The data generation process involves the following steps:
    1. Generate x-values for plotting using linspace to create a range of equally spaced values.
    2. Define the mean and standard deviation parameters for each distribution.
    3. Calculate the probability density function (PDF) for both distributions using stats.norm.pdf().
       The PDF represents the likelihood of a given value occurring in the distribution.
       It is calculated using the formula: f(x) = (1 / (σ * sqrt(2 * π))) * exp(-((x - μ)^2) / (2 * σ^2))
       where μ is the mean, σ is the standard deviation, and x is the value.
    4. Calculate the cumulative distribution function (CDF) for both distributions using stats.norm.cdf().
       The CDF represents the probability that a random variable takes on a value less than or equal to x.
       It is calculated using the formula: F(x) = 0.5 * (1 + erf((x - μ) / (σ * sqrt(2))))
       where erf is the error function.
    5. Return a tuple containing the generated data.

    Returns:
    -------
    tuple: Tuple containing the following elements:
        - numpy array: x values for Equation 1
        - numpy array: x values for Equation 2
        - numpy array: probability density function (PDF) for Equation 1
        - numpy array: probability density function (PDF) for Equation 2
        - numpy array: cumulative distribution function (CDF) for Equation 1
        - numpy array: cumulative distribution function (CDF) for Equation 2
    """
    # Generate x values for plotting
    x_values_e1 = np.linspace(-5, 5, 1000)  # Adjusted x-range for Equation 1
    x_values_e2 = np.linspace(160, 190, 1000)  # Adjusted x-range for Equation 2

    # Define parameters for the normal distributions
    mean_1, std_dev_1 = 0, 1
    mean_2, std_dev_2 = 175, 3

    # Calculate the probability density function (PDF) for the first normal distribution
    pdf_1 = stats.norm.pdf(x_values_e1, loc=mean_1, scale=std_dev_1)

    # Calculate the probability density function (PDF) for the second normal distribution
    pdf_2 = stats.norm.pdf(x_values_e2, loc=mean_2, scale=std_dev_2)

    # Calculate the cumulative distribution function (CDF) for the first normal distribution
    cdf_1 = stats.norm.cdf(x_values_e1, loc=mean_1, scale=std_dev_1)

    # Calculate the cumulative distribution function (CDF) for the second normal distribution
    cdf_2 = stats.norm.cdf(x_values_e2, loc=mean_2, scale=std_dev_2)

    return x_values_e1, x_values_e2, pdf_1, pdf_2, cdf_1, cdf_2


# Generate data
x_values_e1, x_values_e2, pdf_1, pdf_2, cdf_1, cdf_2 = generate_data()

# Create plots
plt.figure(figsize=(20, 10))

# Plot PDFs
plt.subplot(2, 2, 1)
plt.plot(x_values_e1, pdf_1, label='N(0, 1)')
plt.fill_between(x_values_e1, pdf_1, where=(x_values_e1 < 0) & (pdf_1 <= 0.31), color='lightgrey', alpha=0.5)
plt.annotate('P(x < -0.50 | N(0.00, 1.00)) = 0.31', xy=(-1.5, 0.04), xytext=(-4.5, 0.16),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.5'))

# Add the equation as separate text
plt.text(-4.5, 0.27, r'$f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{1}{2} \left(\frac{x - \mu}{\sigma}\right)^2}$',
         fontsize=12, color='black', verticalalignment='top')


plt.xlim(-5, 5)  # Set x-range explicitly
plt.ylim(0, 0.425)  # Adjust y-axis limits for visibility
plt.title('PDF - Equation 1: N(0, 1)')
plt.xlabel('x')
plt.ylabel('f(X)')
plt.legend()

# Set custom y-axis ticker
plt.gca().yaxis.set_major_locator(MultipleLocator(0.05))
plt.gca().set_yticks([0.00, 0.25] + [i * 0.05 for i in range(1, 10) if i != 5])  # Set ticks for every 0.05 interval except 0.45 and 0.50
plt.gca().tick_params(axis='y', which='both', direction='out')  # Set tick direction

plt.subplot(2, 2, 2)
plt.plot(x_values_e2, pdf_2, label='N(175, 3)')
plt.fill_between(x_values_e2, pdf_2, where=(x_values_e2 > 175) & (pdf_2 <= 0.02), color='lightgrey', alpha=0.5)
plt.annotate('P(x > 181.50 | N(175.00, 3.00)) = 0.02', xy=(182, 0.0045), xytext=(180.5, 0.045),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=-.5'))

# Add the equation as separate text
plt.text(162, 0.088, r'$f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{1}{2} \left(\frac{x - \mu}{\sigma}\right)^2}$',
         fontsize=12, color='black', verticalalignment='top')

plt.xlim(160, 190)  # Set x-range explicitly
plt.ylim(0, 0.145)  # Adjust y-axis limits for visibility
plt.title('PDF - Equation 2: N(175, 3)')
plt.xlabel('x')
plt.ylabel('f(X)')
plt.legend()

# Plot CDFs
plt.subplot(2, 2, 3)
plt.plot(x_values_e1, cdf_1, label='N(0, 1)')
plt.axhline(y=0.31, color='black', linestyle='-', xmin=0, xmax=0.45)  # Add horizontal line
plt.axvline(x=-0.5, color='black', linestyle='-', ymin=0, ymax=0.31 / 1, clip_on=False)  # Add vertical line
plt.scatter(-0.5, 0.31, color='white', edgecolor='r', s=75, zorder=5)  # Add circle at intersection point
plt.xlim(-5, 5)  # Set x-range explicitly
plt.ylim(0, 1)  # Adjust y-axis limits for visibility
plt.title('CDF - Equation 1: N(0, 1)')
plt.xlabel('x')
plt.ylabel(r'$\theta(x)=\int_{-\infty}^{x} f(x) \, dx$')
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(x_values_e2, cdf_2, label='N(175, 3)')
plt.axhline(y=0.977, color='black', linestyle='-', xmin=0, xmax=(181 - 160) / (190 - 160), clip_on=False)
plt.axvline(x=181, color='black', linestyle='-', ymin=0, ymax=0.977, clip_on=False)
plt.scatter(181, 0.977, color='white', edgecolor='r', s=75, zorder=5)  # Add circle at intersection point
plt.xlim(160, 190)  # Set x-range explicitly
plt.ylim(0, 1)  # Adjust y-axis limits for visibility
plt.title('CDF - Equation 2: N(175, 3)')
plt.xlabel('x')
plt.ylabel(r'$\theta(x)=\int_{-\infty}^{x} f(x) \, dx$')
plt.legend()

plt.tight_layout()
plt.show()