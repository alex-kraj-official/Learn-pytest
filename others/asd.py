class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def perimeter(self):
        return 2 * self.side_a + 2 * self.side_b
    
    def area(self):
        return self.side_a * self.side_b