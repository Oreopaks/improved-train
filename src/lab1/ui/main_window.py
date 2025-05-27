from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from src.lab1.ui.resources import Ui_MainWindow 
from src.lab1.utils.math_utils import str_to_num_type
from src.lab1.utils.validation import check_div_by_zero

class CalculatorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Инициализация состояния
        self.current_input = ""
        self.previous_value = None
        self.current_operation = None
        self.reset_on_next_input = False
        
        # Подключение кнопок
        self.connect_buttons()
    
    def connect_buttons(self):
        # Цифры
        self.ui.push_0.clicked.connect(lambda: self.add_digit('0'))
        self.ui.push_1.clicked.connect(lambda: self.add_digit('1'))
        self.ui.push_2.clicked.connect(lambda: self.add_digit('2'))
        self.ui.push_3.clicked.connect(lambda: self.add_digit('3'))
        self.ui.push_4.clicked.connect(lambda: self.add_digit('4'))
        self.ui.push_5.clicked.connect(lambda: self.add_digit('5'))
        self.ui.push_6.clicked.connect(lambda: self.add_digit('6'))
        self.ui.push_7.clicked.connect(lambda: self.add_digit('7'))
        self.ui.push_8.clicked.connect(lambda: self.add_digit('8'))
        self.ui.push_9.clicked.connect(lambda: self.add_digit('9'))
        
        # Операции
        self.ui.push_Plus.clicked.connect(lambda: self.set_operation('+'))
        self.ui.push_Minus.clicked.connect(lambda: self.set_operation('-'))
        self.ui.push_Multi.clicked.connect(lambda: self.set_operation('*'))
        self.ui.push_Div.clicked.connect(lambda: self.set_operation('/'))
        
        # Особые кнопки
        self.ui.push_Clear.clicked.connect(self.clear)
        self.ui.push_Res.clicked.connect(self.calculate)
        self.ui.push_Float.clicked.connect(self.add_decimal)
        self.ui.push_Del.clicked.connect(self.delete_last_char)  # Добавлена кнопка удаления


    def add_digit(self, digit):
        if self.reset_on_next_input:
            self.current_input = ""
            self.reset_on_next_input = False
            
        if digit == '0' and not self.current_input:
            self.current_input = "0"  # Явно устанавливаем "0"
        else:
            self.current_input += digit
            
        self.update_display()

    def add_decimal(self):
        if self.reset_on_next_input:
            self.current_input = ""
            self.reset_on_next_input = False
            
        if '.' not in self.current_input:
            if not self.current_input:
                self.current_input = "0"
            self.current_input += '.'
            self.update_display()

    def delete_last_char(self):
        if self.reset_on_next_input:
            return
            
        self.current_input = self.current_input[:-1]
        self.update_display()

    def update_display(self):
        display_text = "0" if not self.current_input else self.current_input
        self.ui.display.setText(display_text[:15])

    def clear(self):
        self.current_input = ""
        self.previous_value = None
        self.current_operation = None
        self.reset_on_next_input = False
        self.update_display()

    def set_operation(self, operation):
        if self.current_input or self.previous_value is not None:
            try:
                # Если предыдущее значение уже есть, сначала вычисляем
                if self.previous_value is not None and self.current_input:
                    self.calculate()
                else:
                    self.previous_value = str_to_num_type(self.current_input if self.current_input else "0")
                
                self.current_operation = operation
                self.reset_on_next_input = True
            except:
                self.current_input = "Error"
                self.previous_value = None
                self.current_operation = None
                self.update_display()

    def calculate(self):
        if self.current_operation and self.previous_value is not None:
            try:
                current_value = str_to_num_type(self.current_input) if self.current_input else self.previous_value
                
                if self.current_operation == '+':
                    result = self.previous_value + current_value
                elif self.current_operation == '-':
                    result = self.previous_value - current_value
                elif self.current_operation == '*':
                    result = self.previous_value * current_value
                elif self.current_operation == '/':
                    if check_div_by_zero(current_value):
                        result = "Error"
                    else:
                        result = self.previous_value / current_value
                
                # Форматируем результат, убирая лишние .0 у целых чисел
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                
                self.current_input = str(result)
                self.previous_value = None
                self.current_operation = None
                self.reset_on_next_input = True
                self.update_display()
            except:
                self.current_input = "Error"
                self.previous_value = None
                self.current_operation = None
                self.update_display()