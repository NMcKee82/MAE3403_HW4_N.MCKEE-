import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Generate x values for plotting
x_values_e1 = np.linspace(-5, 5, 1000)  # Adjusted x-range for Equation 2
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

# Create plots
plt.figure(figsize=(12, 8))

# Plot PDFs
plt.subplot(2, 2, 1)
plt.plot(x_values_e1, pdf_1, label='N(0, 1)')
plt.xlim(-5, 5)  # Set x-range explicitly
plt.ylim(0, 0.5)  # Adjust y-axis limits for visibility
plt.title('PDF - Equation 1: N(0, 1)')
plt.xlabel('x')
plt.ylabel('Density')
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(x_values_e2, pdf_2, label='N(175, 3)')
plt.xlim(160, 190)  # Set x-range explicitly
plt.ylim(0, 0.14)  # Adjust y-axis limits for visibility
plt.title('PDF - Equation 2: N(175, 3)')
plt.xlabel('x')
plt.ylabel('Density')
plt.legend()

# Plot CDFs
plt.subplot(2, 2, 3)
plt.plot(x_values_e1, cdf_1, label='N(0, 1)')
plt.xlim(-5, 5)  # Set x-range explicitly
plt.ylim(0, 1)  # Adjust y-axis limits for visibility
plt.title('CDF - Equation 1: N(0, 1)')
plt.xlabel('x')
plt.ylabel('Probability')
plt.legend()

plt.subplot(2, 2, 4)
plt.plot(x_values_e2, cdf_2, label='N(175, 3)')
plt.xlim(160, 190)  # Set x-range explicitly
plt.ylim(0, 1)  # Adjust y-axis limits for visibility
plt.title('CDF - Equation 2: N(175, 3)')
plt.xlabel('x')
plt.ylabel('Probability')
plt.legend()

plt.tight_layout()
plt.show()
