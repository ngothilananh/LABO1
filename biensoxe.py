# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:49:40 2024

@author: DELL
"""

soxe=int(input("Nhập 4 chữ số của biến số xe: "))
if 1000<=soxe<= 9999:
     hangnghin= soxe//100
     hangtram =(soxe//100)% 10
     hangchuc =(soxe//100)% 10
     hangdonvi =soxe %10
     tong=hangnghin+hangtram+hangchuc+hangdonvi
     print("Số nút của biển số xe là: ", tong)
else:
    print("Dữ liệu không hợp lệ, vui lòng nhập lại ")
   
   
   
   
     
