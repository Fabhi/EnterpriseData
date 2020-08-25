#!/usr/bin/env python3

from gen1 import main as sine
from gen2 import main as cosine

#x = float(input("Enter value of x:"))
x = float(2)
sine = sine(x)
cosine = cosine(x)
print("Sine Value obtained from Mainframe :", sine)
print("Cosine Value obtained from Database :", cosine)
print("sin^2(x) + cos^2(x)")
print("=", sine**2,"+", cosine**2);
print("=", sine**2 + cosine**2 );
