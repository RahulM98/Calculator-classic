## Title: Calculator.py
## Name : Calculator
## @author : Rahul Manna
## Created on : 2020-09-06 20:52:46
## Description : 

import sys
import time
from PyQt5.QtWidgets import QApplication
from UI import calculator_UI

NO_OF_DIGIT = 10        # No of digits calculator can show

class Calculator():
    def __init__(self):
        self.win = calculator_UI()
        self.win.lcd.setNumDigits(NO_OF_DIGIT)

        self.start_calculator()

        for btn in self.win.all_buttons:
            btn.clicked.connect(lambda _,b=btn: self.btn_pressed(b))

    def start_calculator(self):
        self.x = None
        self.y = 0
        self.operator = ""
        self.new_operator = ""
        self.prev_input = ""
        self.display_text = "0"
        self.is_negative = False
        self.is_Dec = False
        self.dec_count = 0

    def evaluate(self):
        if self.x != None and self.y != None and self.operator != '':
            math_error = False
            if self.operator == '+':
                res = self.x + self.y
            elif self.operator == '−':
                res = self.x - self.y
            elif self.operator == '×':
                res = self.x * self.y
            elif self.operator == '÷':
                if self.y != 0:
                    res = self.x / self.y
                else:
                    math_error = True
            
            if math_error:
                self.display_text = "Error"
            else:
                self.x = res
                self.y = 0
                self.display_text = self.x
        else:
            print("None value in evaluate func : x=",self.x,"y=",self.y)
            self.x = self.y
            self.y = 0

    def btn_pressed(self,button):
        pressed_btn = button.text()

        if self.prev_input in ['+','−','×','÷','%','='] and pressed_btn in ['+','−','×','÷','%','=']:
            print("---------Disturbing input-------------")
            if self.prev_input == pressed_btn:
                #if pressed_btn == '.':
                #    self.is_Dec = not self.is_Dec
                #    self.display_text = str(self.y)
                #else:       # else do nothing
                pass
            elif self.prev_input in ['+','−','×','÷','%'] and pressed_btn in ['+','−','×','÷']:
                self.operator = self.new_operator
                self.new_operator = pressed_btn
            elif self.prev_input in ['+','−','×','÷','%'] and pressed_btn == '=':
                self.operator = ''
                self.new_operator = ''
            elif self.prev_input == '=' and pressed_btn in ['+','−','×','÷']:
                #self.operator = self.new_operator
                self.new_operator = pressed_btn
            elif self.prev_input == '=' and pressed_btn == '%':
                self.operator = ''
                self.new_operator = ''
                self.x = self.x / 100
                self.display_text = self.x

        elif pressed_btn == '+':
            self.is_negative = False
            self.is_Dec = False
            self.dec_count = 0
            self.operator = self.new_operator
            self.new_operator = '+'
            self.evaluate()
            
        elif pressed_btn == '−':
            if self.x == None and self.y == 0:
                self.display_text = '-'
                self.is_negative = True
            else:
                self.is_negative = False
            self.is_Dec = False
            self.dec_count = 0
            self.operator = self.new_operator
            self.new_operator = '−'
            self.evaluate()
        
        elif pressed_btn == '×':
            self.is_negative = False
            self.is_Dec = False
            self.dec_count = 0
            self.operator = self.new_operator
            self.new_operator = '×'
            self.evaluate()

        elif pressed_btn == '÷':
            self.is_negative = False
            self.is_Dec = False
            self.dec_count = 0
            self.operator = self.new_operator
            self.new_operator = '÷'
            self.evaluate()
        elif pressed_btn == '.':
            if self.is_Dec == False:
                if self.is_negative:
                    self.display_text = '-' + str(self.y)+'.'
                else:
                    self.display_text = str(self.y)+'.'
            self.is_Dec = True
            
        elif pressed_btn == '%':
            self.y = self.y / 100
            self.display_text = self.y
            self.operator = self.new_operator
            self.new_operator = ''
            self.evaluate()

        elif pressed_btn == '=':
            self.is_negative = False
            self.is_Dec = False
            self.dec_count = 0
            self.operator = self.new_operator
            self.evaluate()
            self.operator = ''
            self.new_operator = ''

        elif pressed_btn == 'Clr':
            self.start_calculator()
        else:
            self.display_text = ''

            if self.display_text != 'Error':
                if self.is_negative:
                    self.display_text = '-'
                
                if self.is_Dec == False:
                    self.y = self.y*10 + int(pressed_btn)
                    self.display_text += str(self.y)
                else:
                    self.dec_count += 1
                    self.y = self.y + (int(pressed_btn)/pow(10,self.dec_count))
                    self.display_text += format(self.y,'.{}f'.format(self.dec_count))
                    
            else:
                self.start_calculator()
                self.y = self.y*10 + int(pressed_btn)
                self.display_text = self.y

        self.prev_input = pressed_btn
        print("Input : ",pressed_btn)

        self.win.lcd.display(self.display_text)
        
app = QApplication(sys.argv)
init_prog = Calculator()
sys.exit(app.exec_())