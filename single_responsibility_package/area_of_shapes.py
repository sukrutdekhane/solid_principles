class Square:
    def __init__(self, side: int):
        self.side = side

    def area(self)->int:
        return self.side*self.side
         


class Circle:
    def __init__(self, radius: int):
        self.radius = radius
    
    def area(self)->float:
        return 3.14*self.radius*self.radius
    
class Triangle:
    def __init__(self, side1:int, side2:int, side3:int):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        return self.side1*self.side2*self.side3


class AreaCalculator:

    def __init__(self, shapes: list):
        self.shapes = shapes

    def sum(self) -> list:
        area = []
        for shape in self.shapes:
            area.append(shape.area())
        return area

    
    def output(self):
        area = self.sum()
        for a in area:
            print(a)


if __name__ == "__main__":
    sq = Square(4)
    c = Circle(4)
    tr = Triangle(3,4,5)
    Area = AreaCalculator([sq,c,tr])
    Area.output()
