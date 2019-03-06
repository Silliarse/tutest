import unittest

def add(a, b):
	if(isinstance(a,(int,float)) and isinstance(b,(int,float))):
		return a+b
	else:
		return "error"
	
print(add(1,3))
print(add(1,2))