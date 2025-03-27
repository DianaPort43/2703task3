def get_area(shape, **params):

    if shape == "rectangle":
        return params["width"] * params["height"]
    elif shape == "square":
        return params["side"] ** 2
    elif shape == "circle":
        from math import pi
        return pi * (params["radius"] ** 2)
    else:
        raise ValueError("Unsupported shape")