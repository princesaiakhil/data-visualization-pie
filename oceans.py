#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 03:02:04 2023

@author: saiakhilpamulaparthy
"""

from matplotlib import pyplot as plt

oceans =  ["Pacific","Atlantic","Indian","Southern","Arctic"]

area = [168.7,85.1,70.5,21.9,15.5]

plt.pie(area,labels= oceans,autopct='%1.1f%%')

plt.axis('equal')

plt.show()