#!/usr/bin/env python3
"""
Program: Thermal Converter LAB 4B
Author: Eliel Cortes
Professor: Prof. Ordonez
Date: 2024-10-03
Description: 
This program converts temperatures between any pair of scales 
from the following list: Celsius (C), Delisle (D), Fahrenheit (F), 
Kelvin (K), Newton (N), Rankine (Ra), Réaumur (Re), Rømer (Ro).
My Sources: 
https://www.cuemath.com/temperature-conversion-formulas/
https://en.wikipedia.org/wiki/Conversion_of_scales_of_temperature

>>> convert_temperature(123.446, 'C', 'C')
123.446

>>> convert_temperature(32, 'F', 'C')
0.0

>>> convert_temperature(100, 'C', 'F')
212.0
"""

# Conversion dictionaries
def to_celsius(scale, temperature):
    """
    Converts a temperature from the given scale to Celsius.
    
    >>> to_celsius('F', 32)
    0.0
    >>> to_celsius('F', 212)
    100.0
    >>> to_celsius('K', 273.15)
    0.0
    >>> round(to_celsius('K', 373.15), 2)
    100.0
    >>> to_celsius('C', 100)
    100
    >>> round(to_celsius('C', 0.0), 2)
    0.0
    >>> to_celsius('Ra', 491.67)
    0.0
    >>> round(to_celsius('Ra', 671.67), 2)
    100.0
    
    >>> to_celsius('Re', 80)
    100.0
    >>> to_celsius('Re', 0)
    0.0
    
    >>> to_celsius('N', 33)
    100.0
    >>> to_celsius('N', 0)
    0.0
    
    >>> to_celsius('Ro', 7.5)
    0.0
    >>> to_celsius('Ro', 60)
    100.0
    
    >>> round(to_celsius('D', 0), 2)
    100.0
    """
    conversion_dict = {
        'C': lambda x: x,
        'F': lambda x: (x - 32) * 5 / 9,
        'K': lambda x: x - 273.15,
        'Ra': lambda x: (x - 491.67) * 5 / 9,
        'Re': lambda x: x * 5 / 4,
        'N': lambda x: x * 100 / 33,
        'Ro': lambda x: (x - 7.5) * 40 / 21,
        'D': lambda x: 100 - (x * 2 / 3)
    }
    return conversion_dict[scale](temperature)

def from_celsius(scale, temperature):
    """
    Converts a temperature from Celsius to the target scale.
    
   
    >>> from_celsius('C', 100.0)
    100.0

    >>> from_celsius('F', 0)
    32.0

    >>> from_celsius('K', 0)
    273.15

    >>> from_celsius('Ra', 0)
    491.67

    >>> from_celsius('Re', 0)
    0.0

    >>> from_celsius('N', 0)
    0.0

    >>> from_celsius('Ro', 0)
    7.5

    >>> from_celsius('D', 0)
    150.0

    >>> from_celsius('C', -40.0)
    -40.0

    >>> from_celsius('F', -40)
    -40.0

    >>> from_celsius('K', -273.15)
    0.0

    >>> round(from_celsius('Ra', 100.0), 2)
    671.67

    >>> from_celsius('Re', 100)
    80.0

    >>> from_celsius('N', 100)
    33.0

    >>> round(from_celsius('Ro', 100), 2)
    60.0

    >>> from_celsius('D', 100)
    0.0
    """
    conversion_dict = {
        'C': lambda x: x,
        'F': lambda x: (x * 9/5) + 32,
        'K': lambda x: x + 273.15,
        'Ra': lambda x: (x * 9/5) + 491.67,
        'Re': lambda x: x * 4/5,
        'N': lambda x: x * 33/100,
        'Ro': lambda x: (x * 21/40) + 7.5,
        'D': lambda x: (100 - x) * 3/2
    }
    return conversion_dict[scale](temperature)

def convert_temperature(temperature, from_scale, to_scale):
    """
    Converts a temperature from one scale to another.
    
    >>> convert_temperature(32, 'F', 'C')
    0.0

    >>> convert_temperature(100, 'C', 'F')
    212.0
    
    >>> convert_temperature(76.12, 'K', 'Ra')
    137.01600000000008
    """
    if from_scale == to_scale:
        return temperature
    
    celsius_value = to_celsius(from_scale, temperature)
    target_value = from_celsius(to_scale, celsius_value)
    
    return target_value

def print_conversion(temperature, from_scale, to_scale, target_value):
    """
    Prints the conversion result.
    """
    if from_scale == 'K':
        print("\n{:.2f}{} = {:.2f}°{}".format(
            temperature, from_scale, target_value, to_scale))
    elif to_scale == 'K':
        print("\n{:.2f}°{} = {:.2f}{}".format(
            temperature, from_scale, target_value, to_scale))
    else:
        print("\n{:.2f}°{} = {:.2f}°{}".format(
            temperature, from_scale, target_value, to_scale))

def main():
    """
    Main function to handle input and output.
    """
    # Explain what the program does
    print("Welcome to my Thermal Converter!")
    print("This program converts temperatures between the following scales:")
    print("Celsius (C), Delisle (D), Fahrenheit (F), Kelvin (K), Newton (N),")
    print("Rankine (Ra), Réaumur (Re), Rømer (Ro).\n")
    
    # Prompt user for input
    temperature = float(input("Temperature to convert: "))
    from_scale = input("Starting scale (C, D, F, K, N, Ra, Re, Ro): ").strip().title()
    to_scale = input("Target scale (C, D, F, K, N, Ra, Re, Ro): ").strip().title()

    # Conversion and printing
    target_value = convert_temperature(temperature, from_scale, to_scale)
    print_conversion(temperature, from_scale, to_scale, target_value)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
