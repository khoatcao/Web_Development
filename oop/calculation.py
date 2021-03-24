from math import pi 
# create a base class  
class Shape(object) :
    def __init__(self,length,width):
        self.length = length 
        self.width = width 
    

class Circle(Shape) :
    def __init__(self,radius) :
        #super().__init__(radius) 
        self.radius = radius 

    def area(self) :
        return pi*self.radius*self.radius  


class Triangle(Shape) :
    def __init__(self,height,length) :
        super().__init__(length,height)
        self.height = height  
    
    def area1(self) :
        return 1/2*self.height*self.length 
class Rectangle(Shape) :
    def __init__(self,length,width) :
        super().__init__(length,width)
    
    def area2(self) :
        return self.length*self.width 

# driver code      
if __name__=="__main__" :
    shape = Shape(5,6)  
    circle = Circle(5)
    triangle = Triangle(5,6)
    rectangle = Rectangle(5,6)

    
