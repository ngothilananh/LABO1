# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 20:06:33 2024

@author: DELL
"""

hinhdang=input("Nhập hình muốn tính toán (VD:vuông(v),chữ nhật(n),tròn(t): ")
if hinhdang == "v":
    canh= float(input("Nhập cạnh:"))
    chuvi= canh*canh
    dientich= canh*4
    print ("Chu vi hình vuông là:", chuvi)
    print("Diện tích hình vuông là:",dientich)
elif hinhdang == "n":
    chieudai=float(input("Nhập chiều dài hình chữ nhật:"))
    chieurong=float(input("Nhập chiều rộng hình chữ nhật:"))
    P= (chieudai+chieurong)*2
    S= chieudai*chieurong
    print("Chu vi hình chữ nhật là:", P)
    print("Diện tích hình chữ nhật là:", S)
elif hinhdang== "t":
    r=float(input("Nhập bán kính hình tròn:"))
    pi= 3.14
    chu=2*pi*r
    dien=pi*(r*r)
    print("Chu vi hình tròn là:", chu)
    print("Diện tích hình tròn là:", dien)
else:
    print("Dữ liệu không hợp lệ")
    
    
    

    
