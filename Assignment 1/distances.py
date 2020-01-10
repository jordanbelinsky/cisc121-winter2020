"""
A module that provides functions related to distance conversions.

Functions:

    miles_to_kiloms(mi)
        Return mi miles in kilometres.

    kiloms_to_miles(km)
        Return km kilometres in miles.
    
    feet_to_metres(ft)
        Return ft feet in metres.

    metres_to_feet(m)
        Return m metres in feet.
    
    inches_to_centims(ins)
        Return ins inches in centimetres.
    
    centims_to_inches(cm)
        Return cm centimetres in inches.

Author: Jordan Belinsky
Date: 2020-01-09
"""

# Miles and Kilometres #
def miles_to_kiloms(mi):
    """
    Return mi miles in kilometres.
    """
    return mi * 1.609

def kiloms_to_miles(km):
    """
    Return km kilometres in miles.
    """
    return km / 1.609


# Feet and Metres #
def feet_to_metres(ft):
    """
    Return ft feet in metres.
    """
    return ft * 0.3048\

def metres_to_feet(m):
    """
    Return m metres in feet.
    """
    return m / 0.3048


# Inches and Centimetres #
def inches_to_centims(ins):
    """
    Return ins inches in centimetres.
    """
    return ins * 2.54

def centims_to_inches(cm):
    """
    Return cm centimetres in inches.
    """
    return cm / 2.54

# Module Testing #
if __name__ == "__main__":
    # Miles and Kilometres #
    print("\nMiles and Kilometres:")
    print(miles_to_kiloms(100))      # 160.9
    print(kiloms_to_miles(160.9))    # 100.0
    print(miles_to_kiloms(10))       # 16.09
    print(kiloms_to_miles(16.09))    # 10.0

    # Feet and Metres #
    print("\nFeet and Metres:")
    print(feet_to_metres(100))       # 30.48
    print(metres_to_feet(30.48))     # 100.0
    print(feet_to_metres(10))        # 3.048
    print(metres_to_feet(3.048))     # 10.0

    # Inches and Centimetres #
    print("\nInches and Centimetres:")
    print(inches_to_centims(100))    # 254.0
    print(centims_to_inches(254))    # 100.0
    print(inches_to_centims(10))     # 25.4
    print(centims_to_inches(25.4))   # 10.0