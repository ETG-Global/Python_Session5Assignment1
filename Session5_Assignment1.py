# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 11:25:05 2018

Session5 Assignment1: Write a function to compute 5/0 and use try/except to 
catch the exceptions.

@author: krishna.i
"""

def tryingexeption():
    try:
            val1 = 5
            val2 = 0
            val3 = val1/val2
            print("\nThe result of Val1/Val2 is:", val3)
    except:
            print("\nOops Result of dividing any number by zero is Infinite and thus invalid..!")

tryingexeption()