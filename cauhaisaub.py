# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 10:36:25 2024

@author: DELL
"""

N=int(input("Nhập N ví dụ: 6785:"))
digits= [int(d) for d in str(N)]
digits.sort()
ketqua = int(''.join(map(str, digits)))
print("Sắp xếp theo thứ tự: ", ketqua)

