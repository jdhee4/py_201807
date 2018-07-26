# def sum(num1, num2):
#     print("sum 함수 :", num1, num2)
#     return num1+num2

# num1 = 10
# num2 = 20
# result = sum(num1,num2)+sum(3,4)
# print(result)

# print(sum(num1,num2))
# print(sum(1,2))
# print("sum 함수 밖", num1, num2)
# print("sum 함수 밖" + num1 + num2) -> Error(숫자와 문자열 결합X, 형변환)

def cart(fruits):
    print("장바구니 안에 다음과 같은 과일이 있습니다.")
    for fruit in fruits:
        print(fruit)

fruits = ['apple','banana','orange']
cart(fruits)
