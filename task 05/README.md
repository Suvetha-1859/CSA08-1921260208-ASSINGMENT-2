Q5 - Functions, Parameters and Scope

Student Details

- Name: Suvetha S
- Register Number: 1921260208
- Course: Python Programming (CSA08)
- Python Version: Python 3.12

Problem Statement

In a college canteen order system, the function "add_item(item, order=[])" uses a mutable default list. Items from previous customers may appear in the next customer's order.

Aim

To understand functions, parameters, return values and scope, and to correct the mutable default argument problem.

Concepts Used

- Functions
- Positional parameters
- Keyword parameters
- Default parameters
- Return values
- Local variables
- Global variables
- Nonlocal variables
- Mutable default arguments

Methodology

1. Identify the problem caused by using an empty list as a default parameter.
2. Use "None" as the default value.
3. Create a new empty list whenever the order is None.
4. Append the item and return the order.
5. Test the function with three customers.
6. Demonstrate local, global and nonlocal variables.

Command Used

python program.py

Expected Result

The corrected function should create independent orders for different customers.

Example:

- Customer 1: Tea
- Customer 2: Vada

Each customer's order should contain only their own items.

Analysis

A default mutable list is created only once when the function is defined. Therefore, changes remain available in later function calls.

Using "None" and creating a new list inside the function avoids this problem.

Conclusion

The program demonstrates the use of functions, parameters and variable scope. Using "None" as a default parameter prevents unwanted sharing of order lists between customers.
