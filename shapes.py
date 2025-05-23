import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        
        # Проверка существования треугольника
        if not (self.a + self.b > self.c and 
                self.a + self.c > self.b and 
                self.b + self.c > self.a):
            raise ValueError("Треугольник с такими сторонами не существует")
        
    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        # Формула Герона
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

class Rectangle:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)
        
    def perimeter(self):
        return 2 * (self.a + self.b)
    
    def area(self):
        return self.a * self.b

class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = float(a)  # верхнее основание
        self.b = float(b)  # нижнее основание
        self.c = float(c)  # левая боковая сторона
        self.d = float(d)  # правая боковая сторона
        
    def perimeter(self):
        return self.a + self.b + self.c + self.d
    
    def area(self):
        # Формула площади трапеции через основания и боковые стороны
        h = math.sqrt(self.c**2 - ((self.b - self.a)**2 + self.c**2 - self.d**2)**2 / (4 * (self.b - self.a)**2))
        return (self.a + self.b) * h / 2

class Parallelogram:
    def __init__(self, a, b, h):
        self.a = float(a)  # сторона
        self.b = float(b)  # сторона
        self.h = float(h)  # высота
        
    def perimeter(self):
        return 2 * (self.a + self.b)
    
    def area(self):
        return self.a * self.h

class Circle:
    def __init__(self, r):
        self.r = float(r)
        
    def perimeter(self):
        return 2 * math.pi * self.r
    
    def area(self):
        return math.pi * self.r**2 