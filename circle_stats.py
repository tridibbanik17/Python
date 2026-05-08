from math import pi

# Get the circle's or sphere's radius in cm as an input argument and output the circle's circumference, area, and sphere's surface area and volume.

def calculate_circle_circumference(radius):
    circumference = 2*pi*radius
    return circumference

def calculate_circle_area(radius):
    area = pi*radius**2
    return area

def calculate_sphere_surface_area(radius):
    surface_area = 4*pi*radius**2
    return surface_area

def calculate_sphere_volume(radius):
    volume = (4/3)*pi*radius**3
    return volume

def print_results():
    radius = float(input("Enter the radius of the circle or sphere in cm: "))
    circumference = calculate_circle_circumference(radius)
    area = calculate_circle_area(radius)  
    surface_area = calculate_sphere_surface_area(radius)
    volume = calculate_sphere_volume(radius)
    print(f"The circumference of the circle is: {round(circumference, 2)} cm")
    print(f"The area of the circle is: {round(area, 2)} cm^2")  
    print(f"The surface area of the sphere is: {round(surface_area, 2)} cm^2")
    print(f"The volume of the sphere is: {round(volume, 2)} cm^3")

print_results()