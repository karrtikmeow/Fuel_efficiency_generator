# KPL Calculator

## Overview of the Project
The **KPL (Kilometers Per Liter) Calculator** is a lightweight Command Line Interface (CLI) utility designed to help vehicle owners track their fuel efficiency. By inputting distance traveled and fuel consumed, the program calculates the precise fuel economy of the vehicle. It is designed to be user-friendly, robust against user input errors, and capable of performing multiple calculations in a single session.

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

## Steps to Install & Run the Project
1. **Prerequisites:** Ensure you have Python installed on your system. You can check this by typing `python --version` in your terminal.
2. **Create the File:**
   * Create a new file named `kpl_calculator.py`.
   * Paste the source code into this file.
3. **Navigate to Directory:** Open your terminal or command prompt and change the directory to where you saved the file:
   ```bash
   cd path/to/your/file