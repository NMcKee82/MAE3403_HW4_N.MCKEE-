import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter, MultipleLocator
from scipy import stats

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

# Create plots
plt.figure(figsize=(20, 10))

# Plot PDFs
plt.subplot(2, 2, 1)
plt.plot(x_values_e1, pdf_1, label='N(0, 1)')
plt.fill_between(x_values_e1, pdf_1, where=(x_values_e1 < 0) & (pdf_1 <= 0.31), color='lightblue', alpha=0.5)
plt.annotate('P(x < -0.50 | N(0.00, 1.00)) = 0.31', xy=(-1.5, 0.04), xytext=(-4.5, 0.16),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.5'))

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
plt.fill_between(x_values_e2, pdf_2, where=(x_values_e2 > 175) & (pdf_2 <= 0.02), color='lightblue', alpha=0.5)
plt.annotate('P(x > 181.50 | N(175.00, 3.00)) = 0.02', xy=(182, 0.0045), xytext=(180.5, 0.045),
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=-.5'))
plt.xlim(160, 190)  # Set x-range explicitly
plt.ylim(0, 0.145)  # Adjust y-axis limits for visibility
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
