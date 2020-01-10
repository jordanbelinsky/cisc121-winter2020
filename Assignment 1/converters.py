"""This program allows the user to perform conversions between
measurement systems for:

    temperatures
    *** Add your conversion module names here ***

Author: R. Linley
Date: 2019-12-18

Modified by: Jordan Belinsky
Section: 002
Student number: 20164936
"""

import menu
import get_int
from temperatures import *
from distances import *
from weights import *


def main():
    # Set up main menu and sub-menus.
    main_menu_choices = ["Temperatures", "Distances", "Weights"]
    temperatures_menu_choices = ["Celsius to Fahrenheit",
                                 "Fahrenheit to Celsius",
                                 "Celsius to Kelvin",
                                 "Kelvin to Celsius",
                                 "Fahrenheit to Kelvin",
                                 "Kelvin to Fahrenheit"]
    distances_menu_choices = ["Miles to Kilometres",
                             "Kilometres to Miles",
                             "Feet to Metres",
                             "Metres to Feet",
                             "Inches to Centimetres",
                             "Centimetres to Inches"]
    weights_menu_choices = ["Tons to Tonnes",
                           "Tonnes to Tons",
                           "Pounds to Kilograms",
                           "Kilograms to Pounds",
                           "Ounces to Grams",
                           "Grams to Ounces"]

    # Loop until user wants to quit.
    while True:
        # Declare main menu
        choice = menu.do_menu("Choose a conversion type:",
                              main_menu_choices)
        if choice is None:  # Did the user choose "Exit?"
            break           # Yes, then exit.
        if choice == 1:     # User chose temperature conversions.
            while True:     # Loop until user wants to return to the main menu.
                choice = menu.do_menu("Choose a temperature conversion",
                                      temperatures_menu_choices)
                if choice is None:
                    break
                if choice is 1:     # Celsius to Fahrenheit chosen.
                    cels = get_int.input_int("\nDegrees Celsius: ")
                    print((f"\n{cels} degrees Celsius is "
                           f"{cels_to_fahr(cels):.1f} "
                           "degrees Fahrenheit."))
                if choice is 2:     # Fahrenheit to Celsius chosen.
                    fahr = get_int.input_int("\nDegrees Fahrenheit: ")
                    print((f"\n{fahr} degrees Fahrenheit is "
                           f"{fahr_to_cels(fahr):.1f} "
                           "degrees Celsius."))
                if choice is 3:     # Celsius to Kelvin chosen.
                    cels = get_int.input_int("\nDegrees Celsius: ")
                    print((f"\n{cels} degrees Celsius is "
                           f"{cels_to_kelv(cels):.1f} "
                           "Kelvin."))
                if choice is 4:     # Kelvin to Celsius chosen.
                    kelv = get_int.input_int("\nKelvin: ")
                    print((f"\n{kelv} Kelvin is "
                           f"{kelv_to_cels(kelv):.1f} "
                           "degrees Celsius"))
                if choice is 5:     # Fahrenheit to Kelvin chosen.
                    fahr = get_int.input_int("\nDegrees Fahrenheit: ")
                    print((f"\n{fahr} degrees Fahrenheit is "
                           f"{fahr_to_kelv(fahr):.1f} "
                           "Kelvin."))
                else:               # Kelvin to Fahrenheit chosen.
                    kelv = get_int.input_int("\nKelvin: ")
                    print((f"\n{kelv} Kelvin is "
                           f"{kelv_to_fahr(kelv):.1f} "
                           "degrees Fahrenheit."))

        if choice == 2:     # User chose distance conversions.
            while True:     # Loop until user wants to return to the main menu.
                choice = menu.do_menu("Choose a distance conversion",
                                      distances_menu_choices)
                if choice is None:
                    break
                if choice is 1:     # Miles to Kilometres chosen.
                    miles = get_int.input_int("\nMiles: ")
                    print((f"\n{miles} miles is "
                           f"{miles_to_kiloms(miles):.1f} "
                           "kilometres."))
                if choice is 2:     # Kilometres to Miles chosen.
                    kiloms = get_int.input_int("\nKilometres: ")
                    print((f"\n{kiloms} kilometres is "
                           f"{kiloms_to_miles(kiloms):.1f} "
                           "miles."))
                if choice is 3:     # Feet to Metres chosen.
                    feet = get_int.input_int("\nFeet: ")
                    print((f"\n{feet} feet is "
                           f"{feet_to_metres(feet):.1f} "
                           "metres."))
                if choice is 4:     # Metres to Feet chosen.
                    metres = get_int.input_int("\nMetres: ")
                    print((f"\n{metres} metres is "
                           f"{metres_to_feet(metres):.1f} "
                           "feet."))
                if choice is 5:     # Inches to Centimetres chosen.
                    ins = get_int.input_int("\nInches: ")
                    print((f"\n{ins} inches is "
                           f"{inches_to_centims(ins):.1f} "
                           "centimetres."))
                else:               # Centimetres to Inches chosen.
                    cms = get_int.input_int("\nCentimetres: ")
                    print((f"\n{cms} Kelvin is "
                           f"{centims_to_inches(cms):.1f} "
                           "inches."))

        if choice == 3:     # User chose weight conversions.
            while True:     # Loop until user wants to return to the main menu.
                choice = menu.do_menu("Choose a weight conversion",
                                      weights_menu_choices)
                if choice is None:
                    break
                if choice is 1:     # Tons to Tonnes chosen.
                    tons = get_int.input_int("\nTons: ")
                    print((f"\n{tons} tons is "
                           f"{tons_to_tonnes(tons):.1f} "
                           "tonnes."))
                if choice is 2:     # Tonnes to Tons chosen.
                    tonnes = get_int.input_int("\nTonnes: ")
                    print((f"\n{tonnes} tonnes is "
                           f"{tonnes_to_tons(tonnes):.1f} "
                           "tons."))
                if choice is 3:     # Pounds to Kilograms chosen.
                    lbs = get_int.input_int("\nPounds: ")
                    print((f"\n{lbs} pounds is "
                           f"{pounds_to_kgrams(lbs):.1f} "
                           "kilograms."))
                if choice is 4:     # Kilograms to Pounds chosen.
                    kgs = get_int.input_int("\nKilograms: ")
                    print((f"\n{kgs} kilograms is "
                           f"{kgrams_to_pounds(kgs):.1f} "
                           "pounds."))
                if choice is 5:     # Ounces to Grams chosen.
                    oz = get_int.input_int("\nOunces: ")
                    print((f"\n{oz} ounces is "
                           f"{ounces_to_grams(oz):.1f} "
                           "grams."))
                else:               # Grams to Ounces chosen.
                    grams = get_int.input_int("\nGrams: ")
                    print((f"\n{grams} grams is "
                           f"{grams_to_ounces(grams):.1f} "
                           "ounces."))

main()  # Initialize main program run
