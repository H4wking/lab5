class Triangle():
    def __init__(self, point1, point2, point3):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.line1 = ((self.point1.x - self.point2.x) ** 2 + (self.point1.y - self.point2.y) ** 2) ** 0.5
        self.line2 = ((self.point2.x - self.point3.x) ** 2 + (self.point2.y - self.point3.y) ** 2) ** 0.5
        self.line3 = ((self.point3.x - self.point1.x) ** 2 + (self.point3.y - self.point1.y) ** 2) ** 0.5

    def is_triangle(self):
        """
        (Triangle) -> bool
        :return: True if Triangle is a triangle, False otherwise.
        """
        if self.line1 + self.line2 < self.line3 or self.line2 + self.line3 < self.line1 or \
           self.line1 + self.line3 < self.line2:
            return False
        return True

    def perimeter(self):
        """
        (Triangle) -> float
        :return: perimeter of the triangle
        """
        return self.line1 + self.line2 + self.line3

    def area(self):
        """
        (Triangle) -> float
        :return: area of the triangle
        """
        p = (self.line1 + self.line2 + self.line3) / 2
        return (p * (p - self.line1) * (p - self.line2) * (p - self.line3)) ** 0.5
