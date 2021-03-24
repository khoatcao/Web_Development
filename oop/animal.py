class Animal(object) :
    # delare constructor 
    def __init__(self,name,age) :
        self.name = name  
        self.age = age 

    def info(self) :
        print(f"My name is",self.name,"and","my age is",self.age)
    
    def is_female(self) :
        return False  
class Duck(Animal) :
    def __init__(self,height,name,age): 
        super().__init__(age,name)
        self.height = height 
    
    def show_info(self) :
        print("My height is " + str(self.height))

    
    def is_over_2m(self) :
        if self.height < 2 :
            print(f"This is a huge duck",self.height," is greater than 2")  
        
        else :
            return None


if __name__ == "__main__": 
    animal = Animal("Tom",3)
    duck = Duck(1,"Jerry",4)

    duck.show_info()
    duck.is_over_2m()