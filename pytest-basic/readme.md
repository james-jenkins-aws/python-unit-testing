## Pytest Basic Example

In this example, we define a Calculator class that has add and subtract methods. We also define a calculator fixture that creates a new Calculator object for each test function.

We then define two test functions: test_add and test_subtract. Each test function takes the calculator fixture as an argument, and uses it to test the add and subtract methods of the Calculator class.

To run this test using pytest, you can save the code in a file called test_calculator.py and then run the following command in your terminal:

`pytest pytests-basic-example.py`