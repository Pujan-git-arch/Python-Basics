

# Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
# area = (1/2)*base*height

# Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
# rectangle area=length*width
# If no shape is supplied then it should take triangle as a default shape


shape = input("Enter the shape (rectangle, triangle): ")

def RectangleArea(l, w):
    area = l * w
    return area

def TriangleArea(b, h):
    area = (1/2) * b * h
    return area

def Area(shape="triangle"):

    if shape == "rectangle":
        l = int(input("Enter the length of the rectangle: "))
        w = int(input("Enter the width of the rectangle: "))
        return RectangleArea(l, w)

    elif shape == "triangle":
        b = int(input("Enter the base of the triangle: "))
        h = int(input("Enter the height of the triangle: "))
        return TriangleArea(b, h)


if shape != "rectangle" and shape != "triangle":
    print("The shape is thought as Triangle. So, the area of the triangle is calculated.")
    shape = "triangle"

print("The shape you entered is:", shape)
print("The area of the", shape, "is:", Area(shape))