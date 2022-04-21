import pytest
from app.calculator_app import Calculator


def test_subtraction_work_for_negative_numbers():
    assert Calculator.subtract(-103, -23) == -80


def test_addition_work_for_positive_numbers():
    assert Calculator.subtract(103, 23) == 80


def test_addition_work_for_positive_negative_numbers():
    assert Calculator.subtract(103, -23) == 126
