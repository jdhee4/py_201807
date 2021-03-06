class Cal():
    def __init__(self, value):
        self.value = value    

    def result(self):
        print(self.value)

    def add(self, input_value):
        self.value += input_value

    def sub(self, input_value):
        self.value -= input_value
    
    def mul(self, input_value):
        self.value *= input_value
    
    def div(self, input_value):
        try:
            self.value /= input_value
        except ZeroDivisionError:
            print("0으로 나눌 수 없어요")
        finally:
            print("나누기 실행 완료")
        
# class SafeCal(Cal):
#     def __init__(self, value):
#         self.value = value
#     def div(self, input_value):
#         if (input_value == 0):
#             self.value = 0
#         else:
#             self.value /=input_value

cal1 = Cal(0)
cal1.add(10)
cal1.result()
cal1.div(0)
cal1.result()

# cal2 = SafeCal(0)
# cal2.add(10)
# cal2.result()
# cal2.div(0)
# cal2.result()

# cal1 = Cal(0)
# cal1.result()