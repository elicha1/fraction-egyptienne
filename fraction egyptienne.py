# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 11:39:38 2018

@author: aicha
"""

from fractions import *
from math import *

def egypt(f):
	e=int(f)
	f-=e
	liste=[e]
	while(f.numerator>1):
		e=Fraction(1,int(ceil(1/f)))
		liste.append(e)
		f-=e
	liste.append(f)
	return liste

a=Fraction(42667,64741)
print(egypt(a))