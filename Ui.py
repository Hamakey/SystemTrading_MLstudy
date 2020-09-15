from Kiwoom import *
import sys
from PyQt5.QtWidgets import *


class Ui_class():
    def __init__(self):
        print("Ui_class입니다.")
        
        self.app =QApplication(sys.argv)
        
        
        
        self.Kiwoom = Kiwoom()
        
        ##사용자가 직접 종료시키지 않는한 계속 실행됨
        
        self.app.exec_()
        
        