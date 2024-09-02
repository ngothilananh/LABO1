# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:40:56 2024

@author: DELL
"""

gio=int(input("Nhập giờ:"))
phut=int(input("Nhập phút:"))
giay=int(input("Nhập giây:"))
if gio <=24:
    print("Giờ hợp lệ")
else:
    print("Giờ không hợp lệ ")
if phut <= 60:
        print("Phút hợp lệ")
else: 
        print("Phút không hợp lệ")
if giay <= 60:
    print("Giây hợp lệ")
else: 
    print("Giây không hợp lệ")
    
    