#!/usr/bin/python3

import math

''' I had a test that was out of 40 and it's fairly trivial to figure out your grade by numerator * 2.5 but for other
tests this can be much more difficult. I wanted to find more coefficients and their accuracy.
'''

for denominator in range(1, 251):
    for constant in range(1, 101):
        if (denominator * constant) % 100 == 0:
            c_div = (denominator * constant)/100
            approx = round(constant/c_div, 1)
            # Assume that one decimal place is used ie. 16.66666 = 16.7
            # Error bars aren't perfect but they give an appoximation
            error = abs(100 - (int(denominator * approx)))
            print('Denominator: ' + str(denominator) + ' Exact: ' + str(constant) + '/' + str(c_div) + " Approx: " + str(approx) + " Error: " + str(error))
            break
