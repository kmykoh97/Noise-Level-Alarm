# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 13:54:31 2018

@author: kmykoh
"""



import winsound



def sample():  
    k = [300,300,75,300,300,300,75,300,300,300,300,75,300,300]
    j = [500,500,37,500,500,500,37,500,500,500,500,37,500,500]
    for i in range(len(k)):
        winsound.Beep(j[i], k[i])
        
def main():
    sample()