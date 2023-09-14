# area_circle.py
# Running this program will prompt the user to enter the radius
# In the area function call, we pass the argument float(r) which
# converts the input string to a float
# The program prints out the area of the circle.

def area(radius):
    return 3.1416 * radius**2

r = input("Enter the radius : ")

print("The area of a circle of radius", r, "is", area(float(r)))


    
