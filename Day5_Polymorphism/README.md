# Day 5: Polymorphism and Singleton in Python

This repository contains practice code for core OOP concepts in Python:
- Polymorphism (method overriding)
- Runtime behavior based on object type
- Basic Singleton pattern

## Project Structure

```text
Day5_Polymorphism/
├── Polymorphism.py
└── ProblemsToSolve/
    ├── Problem1.py
    ├── Problem2.py
    ├── Problem3.py
    └── Problem4.py
```

## What Each File Covers

### `Polymorphism.py`
Contains commented examples of:
- Method overriding (`Animal`, `Dog`, `Cat`)
- Using `super()` in overridden methods
- Runtime polymorphism using a list of parent-type references
- Duck typing

Also includes an active `Singleton` class example that verifies only one instance is created.

### `ProblemsToSolve/Problem1.py` - Payment Processing System
Implements polymorphism with:
- `Payment` (base class)
- `CreditCard` and `UPI` (derived classes overriding `process_payment()`)

A list of payment objects is iterated to call `process_payment()`.

### `ProblemsToSolve/Problem2.py` - Notification System
Implements polymorphism with:
- `Notification` (base class)
- `EmailNotification` and `SMSNotification` (derived classes overriding `send()`)

A list of notification objects is iterated to call `send()`.

### `ProblemsToSolve/Problem3.py` - Shape Area Calculator
Implements polymorphism with:
- `Shape` (base class)
- `Circle` and `Rectangle` (derived classes overriding `area()`)

Shows how different objects provide their own area logic while sharing a common interface.

### `ProblemsToSolve/Problem4.py` - Logger Singleton
Implements a Singleton logger using:
- Class variable `_instance`
- Overridden `__new__()` to return the same object every time
- `log(message)` method

Confirms both created logger objects point to the same instance.

## How to Run

From the project root (`Day5_Polymorphism`), run:

```powershell
python Polymorphism.py
python ProblemsToSolve/Problem1.py
python ProblemsToSolve/Problem2.py
python ProblemsToSolve/Problem3.py
python ProblemsToSolve/Problem4.py
```

## Learning Outcomes

After completing this set, you should be able to:
- Define and use method overriding
- Apply polymorphism with collections of mixed object types
- Understand duck typing basics
- Implement a simple Singleton pattern in Python
