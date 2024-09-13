class Horse:

    def __init__(self, sound = 'Frrr', x_distance = 0):
        self. sound = sound
        self.x_distance = x_distance

    def run(self, dx):
        if isinstance(dx, (int, float)):
            self.x_distance += dx
        else:
            print('Параметр задан неверно.')


class Eagle:

    def __init__(self, sound = 'I train, eat, sleep, and repeat', y_distance = 0):
        self. sound = sound
        self.y_distance = y_distance

    def fly(self, dy):
        if isinstance(dy, (int, float)):
            self.y_distance += dy
        else:
            print('Параметр задан неверно.')


class Pegasus(Horse, Eagle):

    def __init__(self, sound, x_distance, y_distance):
        Horse.__init__(self, sound, x_distance)
        Eagle.__init__(self, sound, y_distance)

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        print(((self.x_distance, self.y_distance)))

    def voice(self):
        print(self.sound)



p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()