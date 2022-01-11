#구구단 출력 프로그램
import sys
number=(1,2,3,4,5,6,7,8,9)

def fun1():
      print('1.홀수 구구단')
      q=[3,5,7,9]
      for i in q:
          print(i,'단')
          for e in number:
              print (i,'*',e,'=',i*e)

    
def fun2():
      print('2.짝수 구구단')
      r=[2,4,6,8]
      for i in r:
          print(i,'단')
          for e in number:
              print (i,'*',e,'=',i*e)

def fun3():
      print('프로그램을 종료합니다.')

while True:
    print('------------------------------------------------------')
    print('\"구구단을 외자, 구구단을 외자\" 프로그램을 실행합니다.')
    print('1.홀수 구구단')
    print('2.짝수 구구단')
    print('3.종료')
    print('------------------------------------------------------')
    a=int(input('숫자를 입력하세요:'))
    if a == 1:
        fun1()
    elif a == 2:
        fun2()
    elif a == 3:
        fun3()
        sys.exit()
    else:
        print("잘못 입력하셨습니다. 1~3 번 숫자를 입력하세요.")

        




"""print("------------------------------------------------------")
print("\"구구단을 외자, 구구단을 외자\" 프로그램을 실행합니다.")
print('1.홀수 구구단')
print('2.짝수 구구단')
print('3.종료')
print('------------------------------------------------------')
a=int(input("숫자를 입력하세요:"))


if a == 1:
    {print("10입니다.")} 
elif a==2 :
    print('1234')
elif a==3 :
 { quit()}
else :
 print("다시 적어주세요")

"""
