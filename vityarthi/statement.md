# Project Statement: KPL Calculator

## Problem Statement

Vehicle owners often struggle to accurately track their fuel economy due to reliance on manual calculations or a lack of immediate, accessible tools. This lack of precise, real-time feedback can lead to delayed detection of vehicle performance issues (e.g., poor engine efficiency) and hinder effective fuel expenditure management. The manual process is also prone to human error.

## Scope of the Project

The KPL Calculator is implemented as a simple, robust Command Line Interface (CLI) application using Python. Its scope is defined by the following boundaries:

### In Scope:

Accepting user inputs for distance traveled (in kilometers) and fuel consumed (in liters).

Performing accurate floating-point arithmetic to compute the Kilometers Per Liter (KPL) ratio.

Implementing exception handling (try...except) to ensure the application remains stable when non-numeric or invalid inputs are provided.

Handling the edge case of division by zero (fuel input = 0) gracefully.

Providing a continuous loop for multiple calculations within a single session.

### Out of Scope:

Data persistence (the application does not save historical usage data).

Development of a Graphical User Interface (GUI) or web interface.

Complex unit conversions (e.g., MPG, L/100km).

### Target Users

The primary users of this project are individuals or small groups who require quick, reliable fuel efficiency data.

Students and New Drivers: Learning to manage vehicle expenses and maintenance.

Daily Commuters: Individuals tracking weekly or monthly fuel usage for personal budgeting.

Small Fleet Operators: Managers who need a simple tool to verify fuel logs and track vehicle performance without complex software.

### High-Level Features

Input Acquisition: A clear, interactive terminal interface that prompts the user for the necessary distance and fuel volume data.

Robust Validation: A core utility feature that checks the validity of the inputs before calculation, ensuring they are numeric and non-zero for the divisor (liters).

Calculation Engine: The module responsible for performing the division and rounding the resulting KPL figure to two decimal places for practical use.

Session Management: The feature that sustains the program's operation, allowing the user to decide whether to perform another calculation or exit.
