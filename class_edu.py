class Parent():
    def __init__(self):
        print("부모 클래스!")
        
        self.money=500000000
        
class Child_1(Parent):
    def __init__(self):
        super().__init__()
        print("첫번째자식")
        
class Child_2(Parent):
    def __init__(self):
        print("두번째자식")
