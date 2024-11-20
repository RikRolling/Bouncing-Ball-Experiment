#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Bouncy Ball Experiment

Ritika Khot, University ID: 10630885

08/10/21

Calculates number of bounces (n) over minimum height (h_min),
using the principle of conservation of energy.
Also, calculates time (total_t) to complete this number of bounces.
Using user inputs h,h_min and eta (where eta represents the efficiency).

"""
import sys
import numpy as np

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~Constant Definition~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GRAVITATIONAL_CONSTANT = 9.81


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~User Inputs~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

height_initial = float(\
                       input('Enter value for initial height of ball (in meters): '))

height_min = float(input(\
                         'Enter value for minimum height (in meters): '))

if height_initial < height_min:

    sys.exit('Error: h and h_min must satisfy inequality h > h_min ')

eta = float(input('Enter value for efficiency : '))

if eta >= 1 or eta <= 0:

    sys.exit('Error: efficiency must be in the range 0 < eta < 1')


number_of_bounces = int(\
                        1/(np.log(eta))*(np.log(height_min) - np.log(height_initial)))


print('number of bounces =', number_of_bounces)

#~~~~~~~~~~~~~~~~~~~~Defining Functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def time_taken_over_all_bounces(bounce_number):
    """


    Parameters
    ----------
    bounce_number : int
       number of bounces
    time_for_each_bounce : float
        time for each bounce (not including time during initial drop)

    Returns
    -------
    None.

    """
    bounce_number = number_of_bounces
    height_per_bounce = height_initial
    time_for_initial_drop = np.sqrt(2 * height_initial/ GRAVITATIONAL_CONSTANT)
    total_time = time_for_initial_drop

    for iterator in range(1, bounce_number + 1):

        height_per_bounce = pow(eta, iterator) * height_initial
        time_per_bounce = \
            2 * np.sqrt(2 * height_per_bounce / GRAVITATIONAL_CONSTANT)
        total_time = total_time + time_per_bounce


    return total_time

TOTAL_TIME = time_taken_over_all_bounces(number_of_bounces)
print("Total time for", number_of_bounces, "bounces (in seconds) =", \
      '{0:4.2f}'.format(TOTAL_TIME))

