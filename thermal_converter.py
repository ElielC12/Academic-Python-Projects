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
"""

# Temperature Conversion Program

def main():
    # Explain what the program does
    print("Welcome to the Thermal Converter!")
    print("This program converts temperatures between the following scales:")
    print("Celsius (C), Delisle (D), Fahrenheit (F), Kelvin (K), Newton (N),")
    print("Rankine (Ra), Réaumur (Re), Rømer (Ro).\n")
    
    # Prompt user for input
    temperature = float(input("Temperature to convert: "))
    from_scale = input("Starting scale (C, D, F, K, N, Ra, Re, Ro): ").strip().upper()
    to_scale = input("Target scale (C, D, F, K, N, Ra, Re, Ro): ").strip().upper()

    # Conversion dictionaries
    to_celsius = {
        'C': lambda x: x,
        'F': lambda x: (x - 32) * 5/9,
        'K': lambda x: x - 273.15,
        'Ra': lambda x: (x - 491.67) * 5/9,
        'Re': lambda x: x * 5/4,
        'N': lambda x: x * 100/33,
        'Ro': lambda x: (x - 7.5) * 40/21,
        'D': lambda x: 100 - (x * 2/3)
    }

    from_celsius = {
        'C': lambda x: x,
        'F': lambda x: (x * 9/5) + 32,
        'K': lambda x: x + 273.15,
        'Ra': lambda x: (x * 9/5) + 491.67,
        'Re': lambda x: x * 4/5,
        'N': lambda x: x * 33/100,
        'Ro': lambda x: (x * 21/40) + 7.5,
        'D': lambda x: (100 - x) * 3/2
    }
    print(f"Debug: from_scale='{from_scale}', to_scale='{to_scale}'")
    # Validate scales
    if from_scale not in to_celsius:
        print(f"Error: Invalid starting scale '{from_scale}' provided.")
        return
    if to_scale not in from_celsius:
        print(f"Error: Invalid target scale '{to_scale}' provided.")
        return

    # conversion
    celsius_value = to_celsius[from_scale](temperature)
    target_value = from_celsius[to_scale](celsius_value)

    # Output the result with degree symbol
    if to_scale == 'K':
        print("\n{:.2f}°{} = {:.2f}{}".format(temperature, from_scale, target_value, to_scale))
    else:
        print("\n{:.2f}°{} = {:.2f}°{}".format(temperature, from_scale, target_value, to_scale))

if __name__ == "__main__":
    main()
    