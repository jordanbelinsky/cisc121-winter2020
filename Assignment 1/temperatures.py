"""
A module that provides functions related to temperature conversions.

Functions:

    cels_to_fahr(deg_c)
        Return deg_c degrees Celsius in degrees Fahrenheit.

    fahr_to_cels(deg_f)
        Return deg_f degrees Fahrenheit in degrees Celsius.

    cels_to_kelv(deg_c)
        Return deg_c degrees Celsius in Kelvin.

    kelv_to_cels(kelv)
        Return kelv Kelvin in degrees Celsius.

    fahr_to_kelv(deg_f)
        Return deg_f degrees Fahrenheit in Kelvin.

    kelv_to_fahr(kelv)
        Return kelv Kelvin in degrees Fahrenheit.

Author: R. Linley
Date: 2019-12-18

Modified by: Jordan Belinsky
Section: 002
Student number: 20164936
"""

# Celsius and Fahrenheit #
def cels_to_fahr(deg_c):
    """
    Return deg_c degrees Celsius in degrees Fahrenheit.
    """
    return (deg_c * 9/5) + 32

def fahr_to_cels(deg_f):
    """
    Return deg_f degrees Fahrenheit in degrees Celsius.
    """
    return (deg_f - 32) * 5/9


# Celsius and Kelvin #
def cels_to_kelv(deg_c):
    """
    Return deg_c degrees Celsius in Kelvin.
    """
    return deg_c + 273.15

def kelv_to_cels(kelv):
    """
    Return kelv Kelvin in degrees Celsius.
    """
    return kelv - 273.15


# Fahrenheit and Kelvin #
def fahr_to_kelv(deg_f):
    """
    Return deg_f degrees Fahrenheit in Kelvin.
    """
    return round((deg_f + 459.67) * 5/9, 8)

def kelv_to_fahr(kelv):
    """
    Return kelv Kelvin in degrees Fahrenheit.
    """
    return round((kelv * 9/5) - 459.67, 3)

# Module Testing #
if __name__ == '__main__':
    # Celsius and Fahrenheit #
    print("\nCelsius and Fahrenheit:")
    print(cels_to_fahr(100))          # 212.0
    print(fahr_to_cels(212))          # 100.0
    print(cels_to_fahr(0))            # 32.0
    print(fahr_to_cels(32))           # 0.0

    # Celsius and Kelvin #
    print("\nCelsius and Kelvin:")
    print(cels_to_kelv(100))          # 373.15
    print(kelv_to_cels(373.15))       # 100.0
    print(cels_to_kelv(0))            # 273.15
    print(kelv_to_cels(273.15))       # 0.0

    # Fahrenheit and Kelvin #
    print("\nFahrenheit and Kelvin:")
    print(fahr_to_kelv(100))          # 310.92777778
    print(kelv_to_fahr(310.92777778)) # 100.0
    print(fahr_to_kelv(0))            # 255.37222222
    print(kelv_to_fahr(255.37222222)) # -0.0

