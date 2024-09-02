# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:43:34 2024

@author: DELL
"""

ngay = int(input("Nhập ngày sinh: "))
thang = int(input("Nhập tháng sinh: "))
nam = int(input("Nhập năm sinh: "))
dinhdang_1= f"{ngay}/{thang}/{nam}"
print("Ngày tháng năm lần lượt là:", dinhdang_1)
dinhdang_2= f"{ngay}/{thang}/{str(nam) [-2:]}"
print("Ngày tháng năm bỏ hai số đầu của năm là:",dinhdang_2)
dinhdang_3= f"{nam}/{thang}/{ngay}"
print("Năm tháng ngày là:", dinhdang_3)





