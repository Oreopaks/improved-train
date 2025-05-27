import pytest
from PyQt5.QtWidgets import QApplication
from src.lab1.ui.main_window import CalculatorWindow

@pytest.fixture(scope="module")
def qt_app():
    app = QApplication([])
    yield app
    app.quit()

@pytest.fixture
def calculator(qt_app):
    calc = CalculatorWindow()
    yield calc
    calc.close()

def test_add_digit(calculator):
    calculator.add_digit('5')
    assert calculator.current_input == "5"
    assert calculator.ui.display.text() == "5"
    
    calculator.add_digit('3')
    assert calculator.current_input == "53"
    assert calculator.ui.display.text() == "53"

def test_add_decimal(calculator):
    calculator.add_decimal()
    assert calculator.current_input == "0."
    assert calculator.ui.display.text() == "0."
    
    calculator.clear()
    calculator.add_digit('5')
    calculator.add_decimal()
    assert calculator.current_input == "5."
    assert calculator.ui.display.text() == "5."
    
    calculator.add_decimal()
    assert calculator.current_input == "5."
    assert calculator.ui.display.text() == "5."

def test_delete_last_char(calculator):
    calculator.add_digit('1')
    calculator.add_digit('2')
    calculator.add_digit('3')
    calculator.delete_last_char()
    assert calculator.current_input == "12"
    assert calculator.ui.display.text() == "12"
    
    calculator.delete_last_char()
    calculator.delete_last_char()
    assert calculator.current_input == ""
    assert calculator.ui.display.text() == "0"

def test_clear(calculator):
    calculator.add_digit('5')
    calculator.set_operation('+')
    calculator.clear()
    
    assert calculator.current_input == ""
    assert calculator.previous_value is None
    assert calculator.current_operation is None
    assert calculator.reset_on_next_input is False
    assert calculator.ui.display.text() == "0"

def test_basic_operations(calculator):
    calculator.add_digit('5')
    calculator.set_operation('+')
    calculator.add_digit('3')
    calculator.calculate()
    assert calculator.ui.display.text() == "8"
    
    calculator.add_digit('1')
    calculator.add_digit('0')
    calculator.set_operation('-')
    calculator.add_digit('2')
    calculator.calculate()
    assert calculator.ui.display.text() == "8"
    
    calculator.add_digit('3')
    calculator.set_operation('*')
    calculator.add_digit('4')
    calculator.calculate()
    assert calculator.ui.display.text() == "12"
    
    calculator.add_digit('1')
    calculator.add_digit('2')
    calculator.set_operation('/')
    calculator.add_digit('3')
    calculator.calculate()
    assert calculator.ui.display.text() == "4"

def test_division_by_zero(calculator):
    calculator.add_digit('5')
    calculator.set_operation('/')
    calculator.add_digit('0')
    calculator.calculate()
    assert calculator.ui.display.text() == "Error"


def test_float_operations(calculator):
    calculator.add_digit('1')
    calculator.add_decimal()
    calculator.add_digit('5')
    calculator.set_operation('*')
    calculator.add_digit('2')
    calculator.calculate()
    assert calculator.ui.display.text() == "3"
    
    calculator.clear()
    calculator.add_digit('1')
    calculator.add_decimal()
    calculator.add_digit('5')
    calculator.set_operation('*')
    calculator.add_digit('1')
    calculator.add_decimal()
    calculator.add_digit('5')
    calculator.calculate()
    assert calculator.ui.display.text() == "2.25"

def test_display_limit(calculator):
    long_number = "12345678901234567890"
    for digit in long_number:
        calculator.add_digit(digit)
    assert len(calculator.ui.display.text()) == 15
    assert calculator.ui.display.text() == "123456789012345"