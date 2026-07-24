import math

class point:
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y

    @property
    #getter
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    # setter
    @x.setter
    def x(self,x):
        self__x = x

    @y.setter
    def y(self,y):
        self.__y = y
    
    def __str__ (self):
        return f"{self.__x} , {self.__y}"
    
    def __add__(self ,other):
        if isinstance(other ,point):
            return point(self.__x + self.__y,
                    self.__y + self.__x)
        
    def calculate_dist(self ,other):
        return math.sqrt(self.__x**2  +  self.__u**2)
    
    

    
    

    




        