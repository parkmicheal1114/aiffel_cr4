
# Code Peer Review Templete
- 코더 : 차정은
- 리뷰어 : 김태원
# PRT(PeerReviewTemplate)
각 항목을 스스로 확인하고 체크하고 확인하여 작성한 코드에 적용하세요.
- [ㅇ] 1.코드가 정상적으로 동작하나요?
- [ㅇ] 2.문제를 제대로 이해했나요?
- [ㅇ] 3.함수가 작동하는 방식을 잘 설명했나요?
- [ㅇ] 4.발생 가능한 에러를 찾아서 디버깅을 했나요?
- [ㅇ] 5.코드를 더 개선시켰나요?

'''python
def palindrome():
 
  word  = input(이름을 입력해 주세요 :   )      #단어 입력 받기   
  reverse_word = ""

                                                  # reverse_word = word[::-1]
  for i in range(1,len(word)+1):                  #단어의 길이만큼 반복하면서 뒤집은 단어 생성   
  reverse_word += word[-i]

  print(뒤집힌 단어는:,reverse_word)
  
  if word == reverse_word:                        #뒤집힌 단어와 기존 단어가 일치하는지 판단   
    print('입력된 단어는 회문입니다.')
  else:
    print('입력된 단어는 회문이 아닙니다.')
'''

# 인덱싱을 활용하여 단어를 역순으로 잘 뒤집었습니다.
# reverse 함수, 슬라이싱 등을 활용하여 반복문 없이 구현할 수 있습니다.
'''
