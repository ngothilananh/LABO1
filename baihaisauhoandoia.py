# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 20:37:01 2024

@author: DELL
"""

a=float(input("Nhập số a: "))
b=float(input("Nhập số b: "))
c=float(input("Nhập số c: "))
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print("Thứ tự tăng dần của các số: ", a,b,c)
