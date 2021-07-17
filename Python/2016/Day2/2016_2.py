#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 02:35:04 2021

@author: shreyas
"""
f = open("input.txt", "r")
Instruction_list=f.readlines()
Keypad=[[1, 2, 3],[4, 5, 6], [7, 8, 9]]
Row=Col=1
Dict={"L":-1,"R":1,"U":-1,"D":1,"\n":0}
Number_list=[]
for each in Instruction_list:
    for every in each:
        if every=="L" or every=="R":
            x=Col+Dict[every]
            if x>=0 and x<=2:
                Col+=Dict[every]
        else:
            y=Row+Dict[every]
            if y>=0 and y<=2:
                Row+=Dict[every]
    Number_list.append(Keypad[Row][Col])
                