# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 13:09:31 2024

@author: DELL
"""
a= float(input("Nhập số a:"))
b= float(input("Nhập sô b:"))
x1 = a + b
x2 = (a**(1/3)) + (b**(1/3))  
x3 = (a * b)**(1/3)  
x4 = a**(1/3)  
x5 = b**(1/3) 
ketqua= ((x1/x2)-x3)/(x4-x5)**2 
print ("Kết quả là: ", round(ketqua,3))