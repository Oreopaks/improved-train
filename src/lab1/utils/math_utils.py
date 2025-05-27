def str_to_num_type(s: str) -> float | int:
    """Конвертирует строку в int или float"""
    try:
        num = float(s)
        return int(num) if num.is_integer() else num
    except (ValueError, TypeError):
        return 0

def calculate(operation: str, a: float, b: float) -> float:
    """Выполняет математическую операцию"""
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else float('nan')
    }
    return operations.get(operation, lambda x, y: 0)(a, b)