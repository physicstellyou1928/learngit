#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 21:13:23 2022

@author: ruth
"""

motorcycle=['honda','yamaha','suzuki']
print(motorcycle)
popped_motorcycle=motorcycle.pop()
print(motorcycle)
print(popped_motorcycle)
del motorcycle[0]
print(motorcycle)
del motorcycle[-1]
print(motorcycle)
