#책정보 출력 프로그램
import sys
#딕셔너리의 하나의 value에 여러개의 value 넣기 Hashmap 형태로 저장됨
book_info ={
    "HarryPotter1":[[1997],[6],[26]], #해리포터1의 3개의 hashmap 만들어짐
    "TheLordOfTheRings":[[1954],[7],[29]],
    "engineering_mathemathics1":[[2018],[2],[28]]
}
#선택메뉴
def menu():
    print('----------------------------------')
    print('원하시는 정보를 선택해주세요.')
    print('1.년')
    print('2.월')
    print('3.일')
    print('4.종료')
    print('----------------------------------')

while True:
    print('원하시는 책을 입력하세요')
    a=str(input('>'))
    if a in book_info:
        while True:
            menu()
            b=int(input())
            if b==1:
                print(book_info[a][0])  #book_info 에서의 자료의 0번째 value 출력
            elif b==2:
                print(book_info[a][1])
            elif b==3:
                print(book_info[a][2])
            elif b==4:
                sys.exit()
            else :
                print()
    else :
        print('제목을 다시 입력해주세요.')

