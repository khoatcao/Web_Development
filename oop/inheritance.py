'''
class Rectangle(object) :
    
    def __init__(self,a,b) :
        self.a = a 
        self.b = b 
    
    def compute_area(self) :
        print("The area of Rectangle is",self.a*self.b)
    

class Triangle(Rectangle) :

    def area(self) :
        print("The area of Triangle is",1/2*self.a*self.b)


# calling object
rectangle = Rectangle(5,6)
triangle = Triangle(7,8)
rectangle.compute_area()
triangle.area()
'''
'''
using super in single inheritance
super.__init__(parameters)
'''
'''
class Rectangle(object) :
    def __init__(self,length,width) :
        self.length = length 
        self.width = width 
    def area(self) :
        print (self.length * self.width   )
    def perimeter(self) :
        return 2*(self.length + self.width) 
# inheritance
class Square(Rectangle) :
    def __init(self,length) :
        super().__init__(length,length)


# calling object 

rectangle = Rectangle(4,5)
square  = Square(4,4)

square.area()



'''
class Animal(object): 
   def __init__(self):
      print ("Animal created")
 
   def whoAmI(self):
      print ("Animal")
 
   def eat(self):
      print ("Eating")
 
 
class Dog(Animal):
   def __init__(self):
      super().__init__()
      print ("Dog created")
 
   def whoAmI(self):
      print ("Dog")
 
   def bark(self):
      print ("Woof!")
 
 
d = Dog()
d.whoAmI()
d.eat()
d.bark()