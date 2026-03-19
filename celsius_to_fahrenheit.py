def celsius_to_fahrenheit(temp: float) -> float:
    """
    Convierte una temperatura de grados Celsius a Fahrenheit.
    """
    fahrenheit = (temp * 9/5) + 32
    
    return float(fahrenheit)