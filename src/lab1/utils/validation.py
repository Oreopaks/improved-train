def check_div_by_zero(value: float) -> bool:
    """Проверяет деление на ноль"""
    return value == 0

def validate_input(input_str: str) -> bool:
    """Проверяет корректность ввода"""
    try:
        float(input_str)
        return True
    except ValueError:
        return False