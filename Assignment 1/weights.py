"""
A module that provides functions related to weight conversions.

Functions:

    tons_to_tonnes(t_us)
        Return t_us US tons in metric tonnes.

    tonnes_to_tons(t_m)
        Return t_m metric tonnes in US tons.

    pounds_to_kgrams(lb)
        Return lb pounds in kilograms.

    kgrams_to_pounds(kg)
        Return kg kilograms in pounds.
    
    ounces_to_grams(oz)
        Return oz ounces in grams.

    grams_to_ounces(g)
        Return g grams in ounces.

Author: Jordan Belinsky
Date: 2020-01-09
"""

# Tons and Tonnes #
def tons_to_tonnes(t_us):
    """
    Return t_us US tons in metric tonnes.
    """
    return round(t_us * 0.907185, 6)

def tonnes_to_tons(t_m):
    """
    Return t_m metric tonnes in US tons.
    """
    return round(t_m * 1.102311, 6)


# Pounds and Kilograms #
def pounds_to_kgrams(lb):
    """
    Return lb pounds in kilograms.
    """
    return round(lb * 0.45359237, 7)

def kgrams_to_pounds(kg):
    """
    Return kg kilograms in pounds.
    """
    return round(kg / 0.45359237, 7)


# Ounces and Grams #
def ounces_to_grams(oz):
    """
    Return oz ounces in grams.
    """
    return round(oz * 28.34952, 4)

def grams_to_ounces(g):
    """
    Return g grams in ounces.
    """
    return round(g / 28.34952, 4)

# Module Testing #
if __name__ == "__main__":
    # Tons and Tonnes #
    print("\nTons and Tonnes:")
    print(tons_to_tonnes(100))          # 90.7185
    print(tonnes_to_tons(90.7185))      # 100.0
    print(tons_to_tonnes(10))           # 9.07185
    print(tonnes_to_tons(9.07185))      # 10.0

    # Pounds and Kilograms #
    print("\nPounds and Kilograms:")
    print(pounds_to_kgrams(100))        # 45.359237
    print(kgrams_to_pounds(45.359237))  # 100.0
    print(pounds_to_kgrams(10))         # 4.5359237
    print(kgrams_to_pounds(4.5359237))  # 10.0

    # Ounces and Grams #
    print("\nOunces and Grams:")
    print(ounces_to_grams(100))         # 2834.952
    print(grams_to_ounces(2834.952))    # 100.0
    print(ounces_to_grams(10))          # 283.4952
    print(grams_to_ounces(283.4952))    # 10.0