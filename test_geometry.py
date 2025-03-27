from math import pi

class ShapeCalculator:

    @staticmethod
    def get_area(shape, **params):
        if shape == "rectangle":
            return params["width"] * params["height"]
        elif shape == "square":
            return params["side"] ** 2
        elif shape == "circle":
            return pi * (params["radius"] ** 2)
        else:
            raise ValueError("Unsupported shape")


print(ShapeCalculator.get_area("rectangle", width=4, height=5)) 
print(ShapeCalculator.get_area("square", side=4))  
print(ShapeCalculator.get_area("circle", radius=3))  