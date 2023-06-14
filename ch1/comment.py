# 주석
"""
여러 줄 주석 처리
"""
'''
여러 줄 주석 처리
'''

# 화면출력 - print() / 변수타입 확인 - type()
print("hello Python!!!")
print("100")
print(25.3)
print(type(100)) # <class 'int'>
print(type("100")) # <class 'str'>
print(type(100.15)) # <class 'float'>
print(type(True)) # <class 'bool'>

# sep : 문자열 사이 구분자 (기본값 spacebar)
print('t','e','s','t') # t e s t
print('t','e','s','t', sep='') # test
print('t','e','s','t', sep='-') # t-e-s-t

# end : 기본값은 엔터, 
print("Welcome To" , end=' ')
print("the black prade")

# format : %s(문자열, 정수, 실수), %d(정수), %f(실수), %c(문자열 하나)
print("%d" % 100)
print("%5d" % 100) # 5자리 맞춰서 출력
print("%05d" % 100) # 5자리 맞춰서 출력 (자릿 수 없는 것은 0으로 채우기)
print()
print("%s" % "hi")
print("%5s" % "hi")
print()
print("%-8.2f" % 123.21)
print("%8.2f" % 123.21)
print("%8.2f" % 123.123456)

# 변수 선언 (타입 선언 안함 - 값에 따라 결정)
number = 3
print("I eat %d apples" % number)
print("I eat ", number , "apple")

print("%d : %s" % (1, "홍길동")) #여러 개 대입할 땐 대입부분에 괄호

print("I eat %s apple" % 2)
print("I eat %s apple" % 3.156)
print("I eat %s apple" % "two")

# 98% 출력
# 특수문자를 출력하려면 2번 반복
print("Error is %d%%" % 98) # Error is 98%

# foamat() 함수
print("\nformat 함수 : {}")
print("{} and {}".format("You","Me")) # You and Me
print("I eat {} apples".format(3))  # I eat 3 apples
print("I eat {0} apples".format(3))  #I eat 3 apples
print("{0} and {1} and {0} ".format("You","Me"))  # You and Me and You
print("{var1} and {var2}".format(var1="You",var2="Me"))  # You and Me
print("{0} and {var2}".format("You",var2="Me"))  #You and Me

# 이스케이프 문자 : \n, \t
print("\n줄바꿈\n연습") #줄바꿈
                        #연습
print("\\ 역슬래쉬") # \ 역슬래쉬
print(r"\n \t \\ 그대로 출력") # \n \t \\ 그대로 출력
print("글자가 '강조' 되는 효과") # 문자 표현시 "",'' 허용
print('글자가 "강조" 되는 효과') # 문자 표현시 "",'' 허용

