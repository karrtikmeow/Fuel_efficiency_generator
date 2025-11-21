# Fuel efficiency generator

## Overview of the Project
The **Fuel efficiency generator** is a lightweight Command Line Interface (CLI) program designed to help vehicle owners track their fuel efficiency. By inputting distance traveled and fuel consumed, the program calculates the precise fuel economy of the vehicle. It is designed to be user-friendly, robust against user input errors, and capable of performing multiple calculations in a single session.

## Features
* **Accurate Calculation:** Computes fuel efficiency using the standard formula (Kilometers / Liters).
* **Smart Rounding:** Automatically formats results to two decimal places for better readability.
* **Input Validation:** Includes error handling to catch non-numeric inputs (e.g., letters or symbols) and prevent program crashes.
* **Zero-Division Protection:** Specifically checks if the fuel input is `0` to avoid mathematical errors.
* **Continuous Operation:** Features a loop mechanism that allows the user to perform multiple calculations without restarting the script.

## Technologies/Tools Used
* **Programming Language:** Python 3.13
* **Libraries:** Standard Python Library (No external dependencies required)
* **Interface:** Command Line / Terminal

## Steps to Run the Project:
1. **Open the Terminal:** In VS Code, go to the menu bar and select **Terminal > New Terminal**.
2. **Start the Program:** In the terminal window that appears at the bottom, type the following command and press Enter: fueleffgenerator.py
