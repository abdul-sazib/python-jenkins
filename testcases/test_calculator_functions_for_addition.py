import allure
import pytest
from app.calculator_app import Calculator


def test_addition_work_for_negative_numbers():
    assert Calculator.add(-103, -23) == -126


def test_addition_work_for_positive_numbers():
    assert Calculator.add(103, 23) == 126


def test_addition_work_for_positive_negative_numbers():
    assert Calculator.add(103, -23) == 80
