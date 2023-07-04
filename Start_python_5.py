# +와 -를 번갈아 출력하기1

n = int(input("출력할 개수 : "))

for i in range(n):
    if(i % 2):
        print('-', end="")
    else:
        print('+', end="")
