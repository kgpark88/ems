import numpy as np

# Define a python list
a_list = [2, 4, -1, 5.5, 3.5, -2, 5, 4, 6.5, 7.5]

# Convert the list into numpy array
an_array = np.array(a_list)

# Compute and print various statistics
print('Mean:', an_array.mean())
print('Median:', np.median(an_array))
print('Range (Max - min):', np.ptp(an_array))
print('Standard deviation:', an_array.std())
print('80th percentile:', np.percentile(an_array, 80))
print('0.2-quantile:', np.quantile(an_array, 0.2))
