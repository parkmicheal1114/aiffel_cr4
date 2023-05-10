Code Peer Review Templete
코더 : 차정은 
리뷰어 :김재림
PRT(PeerReviewTemplate)
각 항목을 스스로 확인하고 체크하고 확인하여 작성한 코드에 적용하세요.

 1.코드가 정상적으로 동작하나요?
 2.문제를 제대로 이해했나요?
 3.함수가 작동하는 방식을 잘 설명했나요?
 4.발생 가능한 에러를 찾아서 디버깅을 했나요?
 5.코드를 더 개선시켰나요?
예시
코드의 작동 방식을 주석으로 기록합니다.
코드의 작동 방식에 대한 개선 방법을 주석으로 기록합니다.
참고한 링크 및 ChatGPT 프롬프트 명령어가 있다면 주석으로 남겨주세요.
# 사칙 연산 계산기

import string

file_line = []
with open('/content/sample_data/06TheAvengers.txt', 'r') as file:
  for line in file:
    temp = line.strip('\n').casefold()
    temp = temp.translate(str.maketrans('', '', string.punctuation))
    temp = ''.join(filter(lambda x: x not in string.punctuation, temp))

    file_line.append(temp)
file_line
string.punctuation

baglist = []
for line in file_line:
  words = line.split()
  for i in range(len(words) - 1):
    gram_temp = (words[i], words[i + 1])
    baglist.append(gram_temp)
baglist


from collections import Counter

countdict = Counter(baglist)

sorted(countdict.items(), key=lambda x: x[1], reverse=True)참고 링크 및 코드 개선 여부
## 제가 헤맸던 부분도 잘 해결하셔서 제가 많이 배웠습니다.
## 코드 짜시는 속도가 정말 빠르신 것 같습니다.
## 아직 해결하지 못한 부분만 하시면 좋을 것 같아요!
