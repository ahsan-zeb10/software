class ScaleneTriangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        # Heron's formula to calculate the area of a scalene triangle
        s = (self.side1 + self.side2 + self.side3) / 2
        area = (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
        return area

    def calculate_perimeter(self):
        perimeter = self.side1 + self.side2 + self.side3
        return perimeter

    def calculate_angles(self):
        # Law of cosines to calculate angles of a scalene triangle
        import math
        angle1 = math.degrees(math.acos((self.side2**2 + self.side3**2 - self.side1**2) / (2 * self.side2 * self.side3)))
        angle2 = math.degrees(math.acos((self.side1**2 + self.side3**2 - self.side2**2) / (2 * self.side1 * self.side3)))
        angle3 = 180 - angle1 - angle2
        return angle1, angle2, angle3

# Sample usage
triangle = ScaleneTriangle(5, 7, 9)
print("Area of the triangle:", triangle.calculate_area())
print("Perimeter of the triangle:", triangle.calculate_perimeter())
print("Angles of the triangle:", triangle.calculate_angles())
