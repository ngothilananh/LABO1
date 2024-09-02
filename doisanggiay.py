# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 16:21:58 2024

@author: DELL
"""

thoigian = input("Nhập giờ phút giây (VD: 1h8p8s): ")
gio= int(thoigian.split ("h")[0])
phut= int(thoigian.split("h")[1].split ("p")[0])
giay=int(thoigian.split("p")[1].split("s")[0])
giosanggiay=gio*3600
phutsanggiay=phut*60
giaydoi=giay
doisanggiay= giosanggiay+phutsanggiay+giaydoi
print("Thời gian đổi sang giây là:", doisanggiay, "giây")

