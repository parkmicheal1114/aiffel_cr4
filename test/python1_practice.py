# # 표현식과 문장

# # 표현식의 예시
# 123                 #숫자
# 1 + 2 + 3           #수식
# 'Hello, world'      #문자열

# # 문장의 예시
# print('Hello, World!')

# # 프로그램의 예시
# overlap = [[1, 2], 3, [[4, 5, 6], 7], 8, 9]

# for element in overlap:
#     print(element)



# # 주석과 출력

# # 주석의 예시
# # print('출력이 안되네요')
# print('출력이 잘 되네요.')

# # 출력의 예시
# a = ['a', 'i', 'f', 'f', 'e', 'l']
# print(a[0])
# print(a[1])
# print(a[2])

# # 한번에 여러개 출력하기
# print('안녕', 111, '123')

# # print()에 아무것도 입력하지 않으면 줄바꿈 함
# print('-'*25)
# print()
# print()
# print('-'*25)



# # 자료형 - 숫자형

# # 정수형(int)
# print(type(5))
# print(type(-1))
# print(type(0))



# #딕셔너리 언패킹

# d1 = {'a': 2, 'b': 3}
# d2 = {'c': 4, 'd': 5}

# result = {**d1, *d2}
# print(result)


# 위치인수, 키워드 인수

def print_nums(a, b, c):
    print(a)
    print(b)
    print(c)
    
print_nums(b=20, c=30, a=10)


def dog_info(name, age, breed):
    print('이름: ', name)
    print('나이: ', age)
    print('품종: ', breed)
    
dog_info('규봉이', 10, '진돗개')