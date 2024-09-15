class Figure:

    sides_count = 0
    
    def __init__(self, color, sides, filled = bool):
        self.__color = color
        self.__sides = self.set_sides(sides)

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
                temp_list.append([side])
        if len(temp_list) == len(sides) == self.sides_count:
            return True
        else:
            return False
        
    def get_sides(self):
        return self.__sides
    
    def __len__(self):
        pirim = 0
        for side in self.__sides:
            pirim += side
        return pirim
    
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides) is True:
            self.__sides = new_sides
            return self.__sides
        elif len(new_sides) == 1:
            self.__sides = [new_sides] * self.sides_count
            return self.__sides
        else:
            self.__sides = [1] * self.sides_count
            return self.__sides
        

class Circle(Figure):

    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color, sides, filled=False)

    def __radius(self):
        return self.__sides[0] / (2 * 3,14)
    
    def get_square(self):
        return self.__sides[0] ** 2 / (4 * 3,14)
    

class Triangle(Figure):

    sides_count = 3

    def __init__(self, color, sides):
        super().__init__(color, sides, filled=False)

    def get_square(self):
        a, b, c = self.__sides
        p = (a + b + c) / 2
        return float((p * (p - a) * (p - b) * (p - c)) ** 0,5)
    

class Cube(Figure):

    sides_count = 12

    def __init__(self, color, sides):
        super().__init__(color, sides, filled=False)

    def get_volume(self):
        return self.__sides[0] ** 3
    
c1 = Circle((200, 200, 100), 10)
print(c1.get_color())
print(c1.get_sides())
print(c1.set_color(150, 150, 180))
print(c1.set_color(180, 260, 280))
#print(len(c1))
print(c1.get_square())