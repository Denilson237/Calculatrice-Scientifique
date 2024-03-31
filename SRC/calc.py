from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit,QShortcut,QSizePolicy
from PyQt5.QtGui import QKeySequence
from PyQt5 import QtCore
from math import sin, cos, radians, tan, pi, cosh, sinh, tanh, log, exp, factorial,acos,asin,atan,log2,log10,degrees

import sys

bouttons = {
    "C" : (1,0,1,1),"del" : (1,6,1,1),"/" : (1,1,1,1),"%" : (8,6,1,1),"7" : (2,0,1,1),"8" : (2,1,1,1),"9" : (2,2,1,1),
    "x" : (2,3,1,1),"4" : (3,0,1,1),"5" : (3,1,1,1),"6" : (3,2,1,1),"-" : (5,2,1,1),"1" : (4,0,1,1),"2" : (4,1,1,1),
    "3" : (4,2,1,1),"+" : (3,3,1,1),"0" : (5,1,1,1), "tanh" : (7,0,1,1),"²⎷" : (1,5,1,1),"x²" : (1,3,1,1),"x³" : (2,6,1,1),
    "asin" : (3,6,1,1),"acos" : (4,6,1,1),"atan" : (5,6,1,1),"x⁻¹" : (7,6,1,1),"π" : (6,2,1,1),"sin" : (3,5,1,1),
    "cos" : (4,5,1,1),"tan" : (5,5,1,1),"e^x" : (7,3,1,1),"^" : (4,3,1,1),"cosh" : (7,2,1,1),"." : (5,0,1,1),"sinh" : (6,3,1,1),
    "=" : (6,5,1,2),")" : (6,1,1,1), "(" : (6,0,1,1),"n!" : (2,5,1,1),"³⎷" : (1,2,1,1),"log2" : (7,5,1,1),"log₁₀" : (8,5,1,1),
    "rad" : (8,0,1,1),"deg" : (8,1,1,1),"+/-" : (8,2,1,1), "10^x" : (8,3,1,1),"e" : (7,1,1,1), "㏑" : (5,3,1,1)
}

operations = ["log₁₀","rad","deg","+/-","10^x","x²","x³","asin","acos","atan","x⁻¹","log2","³⎷","n!","sinh","cosh","tanh","㏑","e^x","+","/","x","^","%","²⎷","sin","cos","tan"]
operation1 = ["(",")","-"]

class Calculatrice(QWidget):
    def __init__(self):
        super().__init__()
        
        self.buttons = {}
        self.setWindowTitle("Calculatrice NGOUMLA DENILSON")
        self.setStyleSheet("""
            background-color: rgb(20, 20, 20);
            color: rgb(220, 220, 220);
            font-size: 18px
        """)
        
        self.main_layaout = QGridLayout(self)
        self.main_layaout.setSpacing(0)
        self.main_layaout.setContentsMargins(0,0,0,0)
        
        self.le_result = QLineEdit("0")
        self.le_result.setMinimumHeight(100)
        self.le_result.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.le_result.setAlignment(QtCore.Qt.AlignRight)
        self.le_result.setEnabled (False)
        self.le_result.setStyleSheet("""
            border: none;
            border-bottom: 2px solid rgb(30,30,30);
            padding: 0 8px;
            font-size: 24px;
            font-weight: bold;
        """)
        self.main_layaout.addWidget(self.le_result, 0,0,1,7)
        
        for button_text,button_position in bouttons.items():
            button = QPushButton(button_text)
            button.setMinimumSize(75,75)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.main_layaout.addWidget(button, *button_position)
            button.setStyleSheet(f"""
                QPushButton {{
                            border:none;
                            font-weight: bold;
                            background-color: {"#1e1e2d" if button_text in operations else "none"}
                }}
                QPushButton:pressed {{background-color: #f31d58;}}""")
            
            if button_text not in ["log₁₀","rad","deg","+/-","10^x","x²","x³","asin","acos","atan","x⁻¹","log2","³⎷","n!","=", "C", "del","%","²⎷","sin","cos","tan","sinh","cosh","tanh","㏑","e^x"]:
                button.clicked.connect(self.operation)
            self.buttons[button_text] = button
        
        self.buttons["del"].clicked.connect(self.nettoyer_t)
        self.buttons["C"].clicked.connect(self.nettoyer_tout)
        self.buttons["="].clicked.connect(self.resultat)
        self.buttons["²⎷"].clicked.connect(self.r_carre)
        self.buttons["sin"].clicked.connect(self.sin)
        self.buttons["cos"].clicked.connect(self.cos)
        self.buttons["tan"].clicked.connect(self.tan)
        self.buttons["sinh"].clicked.connect(self.sinh)
        self.buttons["cosh"].clicked.connect(self.cosh)
        self.buttons["tanh"].clicked.connect(self.tanh)
        self.buttons["㏑"].clicked.connect(self.ln)
        self.buttons["x²"].clicked.connect(self.carre)
        self.buttons["x³"].clicked.connect(self.cube)
        self.buttons["asin"].clicked.connect(self.asin)
        self.buttons["acos"].clicked.connect(self.acos)
        self.buttons["atan"].clicked.connect(self.atan)
        self.buttons["x⁻¹"].clicked.connect(self.inverse)
        self.buttons["log2"].clicked.connect(self.log2)
        self.buttons["³⎷"].clicked.connect(self.r_cubique)
        self.buttons["n!"].clicked.connect(self.factoriel)
        self.buttons["e^x"].clicked.connect(self.e)
        self.buttons["log₁₀"].clicked.connect(self.log10)
        self.buttons["rad"].clicked.connect(self.rad)
        self.buttons["deg"].clicked.connect(self.deg)
        self.buttons["+/-"].clicked.connect(self.inv)
        self.buttons["10^x"].clicked.connect(self.dix_expo)
        self.buttons["="].setStyleSheet("background-color: #1e1e2d; color: #f31d58")
        self.buttons["del"].setStyleSheet("background-color: #1e1e2d;color: #f31d58")
        self.buttons["C"].setStyleSheet("background-color: #1e1e2d;color: #f31d58")
        self.clavier()
    
    def resultat(self):
        a = self.le_result.text()
        try:
            for i in a:
                if i == "^":
                    a = a.replace(i, "**")
                elif i == "x":
                    a = a.replace(i, "*")
                elif i == "π":
                    a = a.replace(i, "3.141592653589793")
                elif i == "e":
                    a = a.replace(i, "2.718281828459045")
            result = eval(a)
              
        except SyntaxError:
            return self.le_result.setText("Error")
        except TypeError:
            return self.le_result.setText("Error")
        except ZeroDivisionError:
            return self.le_result.setText("Error")
        self.le_result.setText(str(result))
    
    def dix_expo(self):
        try:
            a = self.le_result.text()
            a = 10 **(float(a))
        except ValueError:
            return
        self.le_result.setText(str(a))
        
    def inv(self):
        try:
            a = self.le_result.text()
            a = -1*(float(a))
        except ValueError:
            return
        self.le_result.setText(str(a))
    def deg(self):
        try:
            a = self.le_result.text()
            a = degrees(float(a))
        except ValueError:
            return
        self.le_result.setText(str(a))
        
    def rad(self):
        try:
            a = self.le_result.text()
            a = radians(float(a))
        except ValueError:
            return
        self.le_result.setText(str(a))
        
    def log10(self):
        try:
            a = self.le_result.text()
            a = log10(float(a))
        except ValueError:
            return
        self.le_result.setText(str(a))
        
    def log2(self):
        try:
            a = self.le_result.text()
            a = log2(float(a))
        except ValueError:
            return
        self.le_result.setText(str(a))
        
    def acos(self):
        try:
            a = self.le_result.text()
            a = acos(float(a))
        except ValueError:
            return
        self.le_result.setText(str(a))
        
    def asin(self):
        try:
            a = self.le_result.text()
            a = asin(float(a))
        except ValueError:
            return
        self.le_result.setText(str(a))
    
    def atan(self):
        try:
            a = self.le_result.text()
            a = atan(float(a))
        except ValueError:
            return
        self.le_result.setText(str(a))
    
    def factoriel(self):
        try:
            a = self.le_result.text()
            a = factorial(int(a))
        except ValueError:
            return
        self.le_result.setText(str(a))
    def r_cubique(self):
        try:
            a = self.le_result.text()
            a = float(a) ** (1/3)
        except ValueError:
            return
        self.le_result.setText(str(a))
        
    def inverse(self):
        try:
            a = self.le_result.text()
            a = 1/float(a)
        except ValueError:
            return
        self.le_result.setText(str(a))
        
    def cube(self):
        try:
            a = self.le_result.text()
            a = float(a) ** 3
        except ValueError:
            return
        self.le_result.setText(str(a))
    def carre(self):
        try:
            a = self.le_result.text()
            a = float(a) ** 2
        except ValueError:
            return
        self.le_result.setText(str(a))
        
    def sinh(self):
        try:
            a = self.le_result.text()
            a = sinh(float(a))
        except ValueError:
            return
        self.le_result.setText(str(a))
        
    def ln(self):
        try:
            a = self.le_result.text()
            a = log(float(a))
        except ValueError:
            return
        self.le_result.setText(str(a))
        
    def e(self):
        try:
            a = self.le_result.text()
            a = exp(float(a))
        except ValueError:
            return
        self.le_result.setText(str(a))
        
    def cosh(self):
        try:
            a = self.le_result.text()
            a = cosh(float(a))
        except ValueError:
            return
        self.le_result.setText(str(a))
    
    def tanh(self):
        try:
            a = self.le_result.text()
            a = tanh(float(a))
        except ValueError:
            return
        self.le_result.setText(str(a))
        
    def r_carre(self):
        try:
            a = self.le_result.text()
            a = float(a) **(1/2)
        except ValueError:
            return
        self.le_result.setText(str(a)) 
        
        self.le_result.setText(str(a)) 
    def cos(self):
        try:
            a = self.le_result.text()
            a = cos(radians(float(a)))
        except ValueError:
            return
        self.le_result.setText(str(a)) 
    
    def sin(self):
        try:
            a = self.le_result.text()
            a = sin(radians(float(a)))
        except ValueError:
            return
        self.le_result.setText(str(a)) 
        
    def tan(self):
        try:
            a = self.le_result.text()
            a = tan(radians(float(a)))
        except ValueError:
            return
        self.le_result.setText(str(a))  
        
    def nettoyer_t(self):
        if len(self.le_result.text()[:-1]) >= 1 and self.le_result.text() != "Error":
            self.le_result.setText(self.le_result.text()[:-1])
        else:
            self.le_result.setText("0")
    def nettoyer_tout(self):
        self.le_result.setText("0")
         
    def operation(self):
        
        if self.sender().text() in operations:
            if self.le_result.text()[-1] in operations or self.le_result.text()[-1] in operation1 or self.le_result.text() == "0" or self.le_result.text()[-1] == ".":
                return
            
        if self.sender().text() == ".":
            if self.le_result.text()[-1] in operations or self.le_result.text()[-1] == "." or self.le_result.text()[-1] in operation1:
                return 
            
        if self.sender().text() in operation1:
            if self.le_result.text()[-1] in operation1 or self.le_result.text()[-1] in operations or self.le_result.text()[-1] == ".":
                return 
            
        if self.le_result.text() == "0" and self.sender().text() != ".":
            self.le_result.clear()
        self.le_result.setText(self.le_result.text() + self.sender().text())
        
    def clavier(self):
        for button_text, button in self.buttons.items():
            QShortcut(QKeySequence(button_text), self, button.clicked.emit)
        
        QShortcut(QKeySequence("return"), self,self.resultat)
        QShortcut(QKeySequence("backspace"), self,self.nettoyer_t)

app = QApplication(sys.argv)
mac =  Calculatrice()
mac.show()
app.exec()