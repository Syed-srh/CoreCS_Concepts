# Encapsulation in Python

## Overview
This module demonstrates **Encapsulation**, one of the four fundamental principles of Object-Oriented Programming (OOP). Encapsulation is the practice of bundling related attributes and methods into a single entity (class) while hiding internal details from the outside world.

## Concept
Encapsulation involves wrapping data (attributes) and functions (methods) together within a class and controlling access to them through access modifiers.

### Key Purposes
1. **Data Hiding** - Hide the internal implementation details from the outside world
2. **Controlled Access** - Provide controlled access to attributes through methods
3. **Data Protection** - Prevent unauthorized or invalid modifications to data
4. **Maintainability** - Makes code easier to maintain and modify

## Access Modifiers

### 1. Public Access
- **Definition**: Accessible from anywhere (inside and outside the class)
- **Syntax**: No prefix, just `self.attribute_name`
- **Example**:
  ```python
  class Mobile:
      def __init__(self, brand, model, price):
          self.brand = brand      # Public attribute
          self.model = model      # Public attribute
          self.price = price      # Public attribute
  ```

### 2. Private Access
- **Definition**: Restricted access, only accessible within the class
- **Syntax**: Use double underscore prefix `self.__attribute_name`
- **Note**: Python uses name mangling; externally accessible as `_ClassName__attribute_name`
- **Example**:
  ```python
  class Mobile:
      def __init__(self, brand, model, price):
          self.__price = price    # Private attribute
  ```

## Getter and Setter Methods

### Getter Method
- Retrieves the value of a private attribute
- Read-only access to data
- Example:
  ```python
  def get_price(self):
      return self.__price
  ```

### Setter Method
- Updates the value of a private attribute
- Allows validation before updating
- Example:
  ```python
  def set_model_price(self, model, price):
      self.__model = model
      self.__price = price
  ```

## Protection Layer
Encapsulation allows for an additional security layer using validation mechanisms (e.g., secret keys) before allowing sensitive operations:

```python
def set_balance(self, balance, provided_secret_key):
    if provided_secret_key == self.__secret_key:
        self.__balance = balance
    else:
        print("Invalid secret key")
```

## Learning Examples

### Car Class
Demonstrates basic encapsulation with public and private attributes in a Car class.

### Mobile Class
Shows practical use cases including:
- Public attributes (brand)
- Private attributes (model, price)
- Getter methods (get_price)
- Setter methods (set_model_price)
- Validation and protection mechanisms

## Benefits
✅ Protects data integrity  
✅ Improves code security  
✅ Increases code maintainability  
✅ Allows for future modifications without affecting external code  
✅ Provides clear interface for interacting with objects  

## Related Concepts
- **Abstraction**: Hiding complexity, showing only essential features
- **Inheritance**: Inheriting properties and methods from parent classes
- **Polymorphism**: Objects of different classes behaving in different ways

---
*This is part of the CS_by_Nxt course materials on Object-Oriented Programming concepts.*
