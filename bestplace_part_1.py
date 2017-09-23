#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
#Write dunction that return media of 3 input numbers
def median3(a,b,c):
    arr = np.array([a,b,c])
    sorted_arr = np.sort(arr,kind='quicksort')
    return sorted_arr[1]

#---------------------------------------------------
#Write function that return input array without one element
#do not use for loop and new memory

def lost_number(arr):
    sum_of_el = np.sum(arr)
    K = len(arr)
    return (K+1)*(K+2)/2-sum_of_el  #seems it sum of natural numbers
#---------------------------------------------------
