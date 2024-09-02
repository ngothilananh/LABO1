# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:50:31 2024

@author: DELL
"""

nhapchu = input("Nhập một chữ cái: ")
if nhapchu.islower() and len(nhapchu)==1:
    nhapchu=nhapchu.upper()
    print("Chữ hoa là:", nhapchu)
elif nhapchu.upper() and len(nhapchu)==1:
    nhapchu1=nhapchu.lower()
    print("Chữ thường là:", nhapchu1)
else:
    print("Hãy nhập đúng một kí tự ")
    