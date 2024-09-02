# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:16:18 2024

@author: DELL
"""
import math 
a = float(input("Nhập giá trị a: "))
b = float(input("Nhập giá trị b: "))
c = float(input("Nhập giá trị c: "))
denta = b**-4*a*c
if denta>0:
    nghiem1= (-b+ math.sqrt(denta))/2*a
    nghiem2= (-b- math.sqrt(denta))/2*a
    print("Nghiệm của phương trình lần lượt là:", nghiem1, nghiem2)
elif denta == 0:
    nghiemkep= -b/2*a
    print("Phương trình có nghiệm kép:",nghiemkep)
elif denta <0:
    print("Phương trình vô nghiệm:")
    
    