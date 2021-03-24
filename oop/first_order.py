# illustrate : ax + b = 0 => x = -b/a

class Programming :

    # variable initialization
    def __init__(self) : 
        self.a = a
        self.b = b

    def computational(self) :
        if self.b != 0 :
            return  -(self.a / self.b)
        else : 
            return None  

    
a = int(input("Please enter the number A : \n "))
b = int(input("Please enter the number b : \n "))


def Main() :
    program = Programming()
    program.computational()
    
    print("The result is : \n",program.computational())


if __name__=="__main__" :
    Main()

    

