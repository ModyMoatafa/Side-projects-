# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 21:03:05 2023

@author: PC
"""
l=[1,2,3,4,5,6,7,8,9,10]

def binary_search(inputs,start,end,guess):
    if end >=start:
        mid = (end+start)//2
        
        if inputs[mid] == guess:
            return mid
        elif inputs[mid] > guess:
            return binary_search(inputs, start, mid, guess)
        elif inputs[mid] < guess:
            return binary_search(inputs, mid + 1, end, guess)
        
    else:
        return -1
    
x=int(input("Enter your guess:\n"))
result = binary_search(l,0 , len(l)-1, x)
print('your guess is in the list and its index is :' )
print(str(result))