class Figure:

    sides_count = 0
    
    def __init__(self, color, *sides, filled = False):
        self.__color = color
        self.__sides = self.set_sides(sides)
        self.__filled = filled

    def get_color(self):
        return self.__color
    
    def __is_valid_color (self, r, g, b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) is True:
            self.__color = (r, g, b)
            return self.__color
        return
    
    def __is_valid_sides(self, *sides):
        temp_list = []
        for side in sides:
            if isinstance(side, int) and side > 0:
                temp_list.append(side)
        if len(temp_list) == len(sides) == self.sides_count:
            return True
        else:
            return False
        
    def get_sides(self):
        return self.__sides
    
    def __len__(self):
        pirim = 0
        for side in self.__sides:
            if isinstance(side, int):
                pirim += side
            elif isinstance(side, list):
                pirim += sum(side)
        return pirim
    
    def set_sides(self, *new_sides):
        if len(list(new_sides)) == 1:
            self.__sides = list(new_sides[0]) * self.sides_count
            return self.__sides
        elif self.__is_valid_sides(new_sides) is True:
            self.__sides = list(new_sides)
            return self.__sides
        else:
            self.__sides = [1] * self.sides_count
            return self.__sides
        

class Circle(Figure):

    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides, filled=False)

    def __radius(self):
        return self.get_sides()[0] / (2 * 3.14)
    
    def get_square(self):
        return 3.14 * (self.__radius()) ** 2
    

class Triangle(Figure):

    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides, filled=False)

    def get_square(self):
        a = self.get_sides()[0]
        b = self.get_sides()[1]
        c = self.get_sides()[2]
        p = (a + b + c) / 2
        return float((p * (p - a) * (p - b) * (p - c)) ** 0.5)
    

class Cube(Figure):

    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides, filled=False)

    def get_volume(self):
        return self.get_sides()[0] ** 3
    
c1 = Circle((200, 200, 100), 10)
print(c1.get_color())
print(c1.get_sides())
print(c1.set_color(150, 150, 180))
print(c1.set_color(180, 260, 280))
print(len(c1))
print(c1.get_square())

t1 = Triangle((100, 200, 180), 5)
t2 = Triangle((134, 18, 222), 13, 11, 18)
print(t1.get_color())
print(t1.get_sides())
print(t1.set_color(111, 111, 111))
print(t2.set_color(180, 100, 210))
print(len(t2))
print(t1.get_square())
print(t2.get_square())

v1 = Cube((200, 200, 100), 12)
print(v1.get_color())
print(v1.get_sides())
print(v1.set_color(150, 150, 180))
print(v1.set_color(180, 260, 280))
print(len(v1))
print(v1.get_volume())