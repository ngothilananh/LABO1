# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 22:03:45 2024

@author: DELL
"""

N=int(input("Nhập tổng các chữ số: "))
if 10 <=N <=99:
    hangchuc= N//10
    hangdonvi= N%10
    tong=hangchuc+hangdonvi
    print("Tổng các chữ số là: ",tong)
      
   