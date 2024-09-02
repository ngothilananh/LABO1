# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:16:35 2024

@author: DELL
"""

dinh_dang_nguoc_a= input("Nhập ngày/tháng/năm VD 20/8/2021: ")
ngay,thang,nam = dinh_dang_nguoc_a.split("/")
print(f"Ngày:{ngay}  Tháng:{thang}  Năm:{nam}")
dinh_dang_nguoc_b= input("Nhập năm/tháng/ngày VD 2021/8/20: ")
nam,thang,ngay= dinh_dang_nguoc_b.split("/")
print(f"Năm:{nam}  Tháng:{thang}  Ngày:{ngay}")