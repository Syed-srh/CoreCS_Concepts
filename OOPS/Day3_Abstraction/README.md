# Day 3 - Abstraction (Python OOP)

This repository contains beginner-friendly Python examples and practice problems focused on **Abstraction** in Object-Oriented Programming (OOP).

## What You Will Learn

- What abstraction means in OOP
- How to use abstract classes in Python with `abc.ABC` and `@abstractmethod`
- How interface-like behavior can be represented in Python
- How subclasses implement abstract behavior differently

## Project Structure

```text
Day3_Abstraction/
├── Abstraction.py
├── Interface.py
└── ProblemsToSolve/
    ├── Problem1.py
    ├── Problem2.py
    ├── Problem3.py
    
```

## File Overview

### `Abstraction.py`
Demonstrates:
- An abstract base class `vehicle`
- A concrete subclass `Bike`
- Implementation of abstract method `start()`
- Inherited concrete method `fuel_type()`

### `Interface.py`
Demonstrates interface-style design in Python:
- `Engine` and `Gps` as separate contracts
- `Car` implementing both through multiple inheritance

### `ProblemsToSolve/Problem1.py` - Payment System
Includes:
- `Payment` base class with common payment fields
- `UPIPayment` and `CardPayment` subclasses
- Status tracking and payment processing simulation

### `ProblemsToSolve/Problem2.py` - Vehicle System
Includes:
- Abstract class `Vehicle`
- Subclasses `Car` and `Bike`
- Required implementation of `start()` and `stop()`

### `ProblemsToSolve/Problem3.py` - Employee System
Includes:
- Abstract class `Employee`
- Subclasses `Developer` and `Manager`
- Role-specific `work()` implementation

### `ProblemsToSolve/Problem4.py`
Currently empty and available for the next abstraction practice problem.

## How to Run

Make sure Python 3 is installed.

Run any file from the project root:

```bash
python Abstraction.py
python Interface.py
python ProblemsToSolve/Problem1.py
python ProblemsToSolve/Problem2.py
python ProblemsToSolve/Problem3.py
```

> On some systems, use `python3` instead of `python`.

## Requirements

- Python 3.x
- No external libraries required

## Suggested Next Steps

- Convert `Payment` in `Problem1.py` into a true abstract class using `ABC`
- Add validation and error handling (failed payments, invalid inputs)
- Implement `Problem4.py` with a new abstraction scenario (for example: shapes, notifications, or file storage)

## License

This project is for learning and practice.