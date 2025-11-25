# KPL Calculator: Fuel Efficiency Tracker ⛽

## Project Title
**KPL Calculator: Modular Fuel Efficiency Tracker**

### Overview of the Project
This project is a simple, command-line utility built with Python. The main idea behind the KPL Calculator was to stop people from making mistakes when calculating their car's mileage by hand. 

Instead of just making one long script, we split the code up into modules—like one file just for the math and another for checking errors. This lets us show off a **modular design**, which is a key concept we learned, and it makes the program much more stable. The tool's primary function is straightforward: take distance (in KM) and fuel used (in Liters) and give the KPL (Kilometers Per Liter) score right away.

### Key Features (What it Does)
* **Accurate KPL Calculation:** Gets the exact fuel efficiency ratio by performing the division operation.
* **Robust Error Protection:** This is a big one. The code uses `try...except` statements to make sure the program never crashes if you accidentally type letters or symbols instead of numbers.
* **Zero-Safe Logic:** It specifically checks that the fuel input is not zero. If it is, it shows a clear error message instead of causing a fatal division error.
* **Continuous Session Loop:** The program runs until you specifically tell it to stop, allowing you to calculate multiple trips without having to restart the script every time.
* **Clean Output:** Results are rounded to two decimal places and displayed clearly in the terminal.

### Technologies/Tools Used
This project uses a very simple tech stack to focus on core programming concepts:

* **Programming Language:** Python 3.x
* **Code Structure:** Modular Architecture (Code split into dedicated `.py` files for I/O, Validation, and Calculation).
* **Version Control:** Git & GitHub (Used for tracking changes and managing the final project repository).
* **Development Environment:** VS Code (Used for coding and running the terminal interface).

---

### Steps to Install & Run the Project
Since this is a modular project, you need to run the main file (`main.py`) as a module for the imports to work correctly.

**1. Clone the Repository**
Get the code onto your computer from GitHub.
```bash
git clone [https://github.com/YOUR_USERNAME/fuel_efficiency_generator.git](https://github.com/YOUR_USERNAME/fuel_efficiency_generator.git)
```

**2. Open the Terminal**
Open your VS Code Integrated Terminal and make sure you are in the project's root folder (the folder containing `README.md` and the `src` folder).

**3. Run the Modular Code**
Execute the following command:
```bash

### Instructions for Testing

You can easily test the program by trying these specific scenarios:
**Standard Calculation:** Enter **350** for kilometers and **14** for liters. The output should be **25.0 KPL**.

**Invalid Input:** Try entering letters like **abc** for kilometers. The program should display an error (`Please enter a good number`) and ask for input again.

**Zero Division:** Enter **0** for liters. The program should catch this and show `FATAL ERROR: Fuel amount cannot be zero`.

**Negative Value:** Enter **-5** for liters. The program should display `ERROR: The Liters value cannot be negitive`.

**Exit Mechanism:** After finishing a calculation, type **no** when asked if you want to continue. The program should say `Goodbye` and close.

python -m src.main
