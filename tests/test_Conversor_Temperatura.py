import pytest
from src.Conversor_Temperatura import ConversorTemperatura



def test_celsius_a_fahrenheit():
    assert ConversorTemperatura.celsius_a_fahrenheit(0) == 32
    assert ConversorTemperatura.celsius_a_fahrenheit(100) == 212

def test_fahrenheit_a_celsius():
    assert round(ConversorTemperatura.fahrenheit_a_celsius(32), 2) == 0
    assert round(ConversorTemperatura.fahrenheit_a_celsius(212), 2) == 100

def test_celsius_a_kelvin():
    assert ConversorTemperatura.celsius_a_kelvin(0) == 273.15
    assert ConversorTemperatura.celsius_a_kelvin(-273.15) == 0

def test_kelvin_a_celsius():
    assert ConversorTemperatura.kelvin_a_celsius(273.15) == 0
    assert ConversorTemperatura.kelvin_a_celsius(0) == -273.15
