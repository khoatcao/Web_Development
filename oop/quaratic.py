import numpy as np   
class Programming :
    
    # variable initialization
    def __init__(self) : 
        self.a = a
        self.b = b
        self.c = c   
        #self.delta = delta
    
    # solve first_order 
    def is_zero(self) :
        if self.a == 0 :
            return -(self.b)/(self.c)
        else : 
            pass
            #print("This is a quadratic equation \n")
    def computation(self) :
        self.delta = ((self.b)*(self.b)) - (4*self.a*self.c)

        # conditional
        if self.delta < 0 :
            print(" Error programming ")
        elif self.delta == 0 :
            print("The result is",-self.b/(2*self.a))
        elif self.delta >= 0 :
            print(" The result x1 :",(-self.b + np.sqrt(self.delta))/(2*self.a) )
            print(" The result x2 : ",(-self.b - np.sqrt(self.delta))/(2*self.a))
        
a = int(input("Please enter the number A :  "))
b = int(input("Please enter the number b :  "))
c = int(input("Please enter the number c :  "))

def Main() :
    program = Programming()

    program.is_zero()
    program.computation()


if __name__=="__main__" :
    Main() 

