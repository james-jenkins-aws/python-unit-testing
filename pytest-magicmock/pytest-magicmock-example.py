from unittest.mock import MagicMock
import pytest

class MyClass:
    def my_method(self):
        return "Hello, world!"

def test_my_function():
    my_obj = MyClass()
    my_mock = MagicMock(return_value="Mocked value")
    
    # Replace my_obj.my_method with the mock object
    my_obj.my_method = my_mock
    
    # Test that the mock object is called correctly
    assert my_obj.my_method() == "Mocked value"
    
    # Test that the original method still works as expected
    my_obj = MyClass()
    assert my_obj.my_method() == "Hello, world!"