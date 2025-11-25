# ⛽ Project Statement: KPL Calculator

## 💡 Problem Statement

Every day, vehicle owners need to know their **fuel efficiency**, but calculating **Kilometers Per Liter (KPL)** is often slow and, frankly, annoying. Most people just guess or rely on tricky calculator apps. The biggest issue is that **manual tracking is full of mistakes**—one small arithmetic error, or entering the wrong number, completely messes up the result.

This lack of a fast, reliable tool means drivers can't quickly spot when their engine performance drops or when they're wasting too much fuel. We need a solution that is **instant, simple to use, and unbreakable**, so users always get the correct number without dealing with crashes or confusing interfaces.

---

## 🛠️ Scope of the Project

This project focuses on delivering a core utility function through a **stable, modular Python Command Line Interface (CLI)**.

### **✅ In Scope:**

* Accepting **distance (km)** and **fuel (liters)** data.
* Calculating and displaying the **KPL ratio**.
* Implementing **robust checks** to handle non-numeric inputs (letters) and critical errors (division by zero).
* Providing a **continuous loop** for repeat calculations.

### **❌ Out of Scope:**

* Any kind of **graphical interface (GUI)**.
* Saving historical data to a file or database.
* Advanced features like unit conversions (e.g., MPG).

---

## 🎯 Target Users

We designed this tool for anyone who needs to quickly and reliably check their fuel consumption:

* **Students and Budgeters:** People who need to track every liter for personal finance.
* **Small Business Owners:** Managers who need a quick check on vehicle usage logs without using complex software.
* **Basic Computer Users:** Anyone who prefers a simple, functional terminal tool over a confusing app.

---

## ✨ High-Level Features

| Feature | Description |
| :--- | :--- |
| **Fast Input Interface** | The system immediately prompts for the two required numbers (KM and Liters). |
| **Crash Protection** | Includes safety features that prevent the program from failing due to **bad data** (like typing words). |
| **Zero-Proof Math** | Ensures that calculating the KPL is mathematically sound by automatically catching and rejecting **zero-fuel inputs**. |
| **Repeatable Sessions** | The application keeps running until the user manually chooses to exit. |
