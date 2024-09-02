# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:01:16 2024

@author: DELL
"""

a=float(input("Nhập giá trị a:"))
b=float(input("Nhập giá trị b:"))
if a !=0:
    nghiemduynhat= -b/a
    print("Phương trình có nghiệm duy nhất là:",nghiemduynhat)
else:
    if b == 0:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
        