# 세 정수를 입력받아 중앙 값 구하기 1

def find_median(number1,number2,number3):

    if number1 >= number2:
        if number2 >= number3:
            return number2
        elif number1 <= number3:
            return number1
        else:
            return number3

    elif number1 >= number3:
        return number1
    elif number2 >= number3:
        return number3
    else:
        return number2

a = int(input("첫 번째 정수를 입력하세요:"))
b = int(input("두 번째 정수를 입력하세요:"))
c = int(input("세 번째 정수를 입력하세요:"))

print(f"중앙값은 : {find_median(a,b,c)} 입니다.")