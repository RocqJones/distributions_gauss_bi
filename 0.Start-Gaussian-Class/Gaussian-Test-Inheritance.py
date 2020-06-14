import unittest
from GaussianMain import Distribution
from GaussianMain import Gaussian

# initialize two gaussian distributions
gaussian_one = Gaussian(25, 3)
gaussian_two = Gaussian(30, 2)

# initialize a third gaussian distribution reading in a data efile
gaussian_three = Gaussian()
gaussian_three.read_data_file('numbers.txt')
gaussian_three.calculate_mean()
gaussian_three.calculate_stdev()

print("*********************************************")

# print out the mean and standard deviations
print(gaussian_one.mean)
print(gaussian_two.mean)

print(gaussian_one.stdev)
print(gaussian_two.stdev)

print(gaussian_three.mean)
print(gaussian_three.stdev)

print("*********************************************")

# plot histogram of gaussian three
gaussian_three.plot_histogram_pdf()

print("*********************************************")

# add gaussian_one and gaussian_two together
gaussian_one + gaussian_two