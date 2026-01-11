# Various programs to do calculations using formulas found in AP Statistics
#
# Ex. Standard Deviation of the difference of two sampling distributions

import math

# find standard deviation for difference of sampling distributions of proportions
def SD_proportions(p1, p2, n1, n2):
    standard_deviation = math.sqrt((p1*(1-p1))/n1 + (p2*(1-p2))/n2)
    return standard_deviation

# find standard deviation for difference of sampling distributions of means
def SD_means(sigma1, sigma2, n1, n2):
    standard_deviation = math.sqrt((sigma1**2)/n1 + (sigma2**2)/n2)
    return standard_deviation

def find_side_c(a, b, angle_c):
    angle_c_rad = math.radians(angle_c)
    c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(angle_c_rad))
    return c

def main():
    print("STATS")
    print("Choose one of the following:")
    print("1. Calculate the standard deviation of the difference of two sampling distributions of proportions")
    print("2. Calculate the standard deviation of the difference of two sampling distributions of means")
    choice = int(input("Enter your choice (1 or 2): "))

    if choice == 1:
        print("Standard Deviation of the Difference of Two Sampling Distributions of Proportions")
        print("**Percents must be entered as decimals**")
        p1 = float(input("Enter the value of p1 (the probability for population 1): "))
        p2 = float(input("Enter the value of p2 (the probability for population 2): "))
        n1 = float(input("Enter the value of n1 (the population size of population 1): "))
        n2 = float(input("Enter the value of n2 (the population size of population 2): "))
        standard_deviation = SD_proportions(p1, p2, n1, n2)
        print("The standard deviation of the difference of the two sampling distributions is:", round(standard_deviation, 4))
    elif choice == 2:
        print("Standard Deviation of the Difference of Two Sampling Distributions of Means")
        print("**Percents must be entered as decimals**")
        sigma1 = float(input("Enter the standard deviation of population 1: "))
        sigma2 = float(input("Enter the standard deviation of population 2: "))
        n1 = float(input("Enter the value of n1 (the population size of population 1): "))
        n2 = float(input("Enter the value of n2 (the population size of population 2): "))
        standard_deviation = SD_means(sigma1, sigma2, n1, n2)
        print("The standard deviation of the difference of the two sampling distributions is:", round(standard_deviation, 4))
        
    else:
        print("Invalid choice. Exiting...")
        exit()

main()
