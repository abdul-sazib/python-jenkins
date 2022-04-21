import allure
import pytest
from app.calculator_app import Calculator


@allure.step('adding two negative numbers should produce negative result')
@allure.severity_level(allure.severity_level.CRITICAL)
def test_subtraction_work_for_negative_numbers():
    assert Calculator.subtract(-103, -23) == -80


@allure.step('adding two positive numbers should produce positive result')
@allure.severity_level(allure.severity_level.CRITICAL)
def test_addition_work_for_positive_numbers():
    assert Calculator.subtract(103, 23) == 80


@allure.step('adding a positive number with a negative number')
@allure.severity_level(allure.severity_level.MINOR)
def test_addition_work_for_positive_negative_numbers():
    assert Calculator.subtract(103, -23) == 126
