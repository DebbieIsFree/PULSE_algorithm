# 예외처리 추가 : '1a' 같은 문자가 입력되면 바로 종료

cur = input()

if cur[0].isalpha() == False :
    exit(0)


y = ord(cur[0])     # ord() : 문자의 유니코드 반환
x = int(cur[1])     # x (row), y(col)


# 오른쪽 , 위 :  (+)
# 왼쪽, 아래 : (-)
dir = [(2,1),(2, -1),(-2,1),(-2,-1),(1,-2),(-1,-2),(1,2),(-1,2)]

count = 0

for i in dir:
    xx = x + i[0]
    yy = y + i[1]

    if yy < 97 or yy > 104 or xx < 1 or xx > 8:
        continue
    count += 1

print(count)



