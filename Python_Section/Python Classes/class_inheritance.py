class MyClass1:
    def __init__(self, class_1_input_1) -> None:
        print("init of class 1")
        self.prop_class1 = 10
        self.class_1_input_1 = class_1_input_1
        print(self.class_1_input_1)
    
    def method_1_class_1(self):
        print("method_1_class_1")


class MyClass2(MyClass1):

    def __init__(self, input2_in_1) -> None:
        #super tells it to start init of inherited class
        super().__init__(input2_in_1)
        print('init of class 2')

    def method_1_class_2(self):
        print("method_1_class_2")



object2 = MyClass2('ABC')


