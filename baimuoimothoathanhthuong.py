# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:45:02 2024

@author: DELL
"""

kitu=input("Nhập 1 kí tự thường: ")
if kitu.islower() and len(kitu)==1:
    kitu= kitu.upper()
    print("Kí tự hoa là: ", kitu)
else:
    print("Vui lòng nhập một kí tự ")