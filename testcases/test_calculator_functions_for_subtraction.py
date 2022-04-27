import allure
import pytest
from app.calculator_app import Calculator


class TestClass:

    @allure.step('adding two negative numbers should produce negative result')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_subtraction_work_for_negative_numbers(self):
        pytest.driver.get('https://stackoverflow.com/questions/60296134/how-to-access-instance-variable-inside-classmethod')
        assert Calculator.subtract(-103, -23) == -80

    @allure.step('adding two negative numbers should produce negative result')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_subtraction_work(self):
        assert Calculator.subtract(-103, -23) == -80


""" @allure.step('adding two positive numbers should produce positive result')
@allure.severity(allure.severity_level.CRITICAL)
def test_addition_work_for_positive_numbers():
    assert Calculator.subtract(103, 23) == 807 """
