# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 17:57:59 2024

@author: DELL
"""


a = int(input("Nhập giá trị a: "))
b = int(input("Nhập giá trị b: "))
c = int(input("Nhập giá trị c: "))
d = int(input("Nhập giá trị d: "))
if a == b == c == d:
    print("Bốn số bằng nhau, vui lòng nhập lại")
else:
    if a >= b and a >= c and a >= d:
        solonnhat = a
    elif b >= a and b >= c and b >= d:
        solonnhat = b
    elif c >= a and c >= b and c >= d:
        solonnhat = c
    else:
        solonnhat = d
    
    print("Số lớn nhất là:", solonnhat)
