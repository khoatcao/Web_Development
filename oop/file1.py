import pandas as pd 
import numpy as np    


class Calculator :
      # define constructor and init variables
    def __init__(self,a,b) :
        self.a = a
        self.b = b  
        
    # add two numbers
    def add(self) :
        return self.a + self.b  
    # multiply two numbers
    def mul(self) : 
        return self.a * self.b
    def sub(self) : 
        return self.a - self.b
    def div(self) :
        return self.a/self.b

# define int type
a = int(input("Please enter value of a : \n"))
b = int(input("Please enter value of b : \n")) 

# define main function
def Main() :
    # creating an object to Calculator
    cal = Calculator(a,b) # calling object
    cal.add() 
    cal.mul()
    cal.sub()
    cal.div() 

    print("Add two numbers in python       : \n", cal.add())
    print("Multiply two numbers in python  : \n", cal.mul())
    print("Substract two numbers in python : \n", cal.sub()) 
    print("Divide two numbers in python    : \n", cal.div())
if __name__=='__main__' :
    Main()    



