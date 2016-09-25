#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Spyder-demo-script.py

This script defines a few variables to demonstrate using the Spyder IDE's
object inspector and variable explorer.

Created on Sat Sep 24 23:23:11 2016

@author: David Whipp
"""

# Define a few variables
BigNumber = 123456789
BigFloat = 123456789.0123456789
DummyString = "Tropical Hot Dog Night"
ChocolateIsGood = 3

# Define a line containing the variables above
OddList = [BigNumber, BigFloat, DummyString, ChocolateIsGood]

# Modify one variable (note the value for this in the list)
BigNumber = 1048576    # One megabyte in bytes

# Print the current value of BigNumber
print("BigNumber is now", BigNumber)

# Print BigNumber in binary
print("BigNumber is binary is", bin(BigNumber))