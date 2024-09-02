# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 16:57:13 2024

@author: DELL
"""

a=int(input("Nhập số nguyên a: "))
b=int(input("Nhập số nguyên b: "))
c=int(input("Nhập số nguyên c: "))
if a >= b and a >= c:
    solonnhat= a 
elif b >= a and b >= c:
    solonnhat=b
else:
    solonnhat=c
print("Số lớn nhất là:", solonnhat)
if a <= b and a <= c:
    sonhonhat=a
elif b <= a and b <= c:
    sonhonhat=b
else:
    sonhonhat=c 
print("Số nhỏ nhất là:", sonhonhat)
    


    


