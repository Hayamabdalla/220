"""
name: Hayam Abdalla
mean.py


problem:calculating the rms average , harmonic mean and geometric mean

certification of authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def main():
    numbers_of_values = eval(input("how many numbers of values to be entered?"))
    # numbers of values to be input by user
    added = 0
    denom = 0
    multiply = 1

    # loop
    for _ in range(numbers_of_values):
        value = eval(input("enter the value:"))
        #  value is for the values that the user input

        # calculation
        # for rms mean
        added = added + (value ** 2)

        # for harmonic mean
        reciprocal = 1 / value
        denom = denom + reciprocal
        # for geometric mean
        multiply = multiply * value
    # mean calculation
    rms_mean = round(math.sqrt(added / numbers_of_values), 3)
    harmonic_mean = round((numbers_of_values / denom), 3)
    geometric_mean = round(multiply ** (1 / numbers_of_values), 3)

    # print
    print(rms_mean)
    print(harmonic_mean)
    print(geometric_mean)


if __name__ == "__main__":
    main()
