# -*-coding:utf-8

# 반복문 while, for
# 기존 언어의 while문과 기능과 사용법이 동일함
# while 문 외부에 카운트 변수를 선언, while 내부에 변수를 카운트, while 문 옆에 조건을 입력
# while의 조건 부분에 괄호를 사용하지 않음
# if 문과 동일하게 들여쓰기를 무조건 맞춰줘야 함

treeHit = 0

while treeHit < 10:
    treeHit = treeHit + 1 # treeHit += 1 # 변수 카운트
    print("나무를 %d번 찍었습니다." % treeHit) # print("나무를 {0}번 찍었습니다.".format(treeHit))
    if treeHit == 10:
        print("나무가 넘어갑니다.")

# 반복문 탈출하기 (break)
# break를 만나면 가장 기까운 반복문에서 탈출함
# 기존 언어의 break 문과 기능 및 사용법이 동일함

print()

coffee = 10
money = 300

# 숫자형은 0 이 아니면 모두 True이므로 while을 실행함
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1 # coffee =- coffee
    print("남은 커피의 양은 {0}개입니다.".format(coffee))
    
    # not 연산자를 사용하여 coffee의 값이 0이 아닐 경우는 그냥 넘어가고, coffee의 값이 0일 경우 아래의 내용을 실행함 
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break # 가장 가까운 반복문을 탈출

# 자바
# while(money > 0) {
#    System.out.println();

#    if (!coffee) {
#        break
#    }
# }

print()

coffee = 1

# while의 조건문에 True를 입력하면 while의 반복 조건이 무조건 True이므로 while은 무한루프에 빠짐
while True:
    money = int(input("돈을 넣어주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 {0}를 주고 커피를 줍니다.".format(money - 300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 {0}개입니다".format(coffee))
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
    
# 조건에 맞지 않을 경우 맨 처음으로 돌아가기 (continue)
# 기존 다른 언어의 continue 문과 기능과 사용법이 동일함

a = 0

while a < 10:
    a += 1

    if a % 2 == 0:
        continue

    print(a)

print()
# 문제 2) 사용자가 입력한 숫자에 해당하는 구구단을 출력하세요

dan = input("출력할 구구단의 단수를 입력하세요 : ")
# 자바의 형변환과 다름
dan = int(dan)
i = 1 # 카운트 변수 선언
while i < 10:
    print("{0} * {1} = {2}".format(dan, i, dan * i))
    i += 1

print()
# 문제 3) 2중 while 문을 사용해서 구구단 전체를 출력하세요

dan = input("단수를 입력하세요 : ")
dan = int(dan)

i = 1
j = 1
while i < 9:
    i = i + 1   
    while j < 9:
        j = j + 1
        print("{0} * {1} = {2}".format(i,j,i*j))
    j = 1

print()
# 문제 4) while문과 list를 사용하여 로또 번호 자동 생성 프로그램을 만드세요
# 6개의 숫자를 랜덤으로 출력 받음
# 발생된 로또 번호를 리스트 변수 lotto 에 저장
# 마지막에 리스트 lotto를 화면에 출력

# 난수 발생을 위한 모듈
import random
# 범위 내의 난수 발생
val = random.randint(1, 45)

lotto = []

print("이번 주 로또 번호 : ")

num1 = 0
while num1 < 6:
    num = random.randint(1, 45)
    lotto.append(num)

    num1 = num1 + 1

print(lotto)
# 여기까지하면 숫자가 중복이 될 수도 있다.