class ConversorTemperatura:
    @staticmethod
    def celsius_a_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_a_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def celsius_a_kelvin(celsius):
        return celsius + 273.15

    @staticmethod
    def kelvin_a_celsius(kelvin):
        return kelvin - 273.15


if __name__ == "__main__":
    celsius = 25
    print(f"{celsius}°C en Fahrenheit: {ConversorTemperatura.celsius_a_fahrenheit(celsius)}°F")
    print(f"{celsius}°C en Kelvin: {ConversorTemperatura.celsius_a_kelvin(celsius)}K")
