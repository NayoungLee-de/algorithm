s = list(input())
s.sort()
answer = []
sum = 0

for i in s:
    if i.isalpha():
        answer.append(i)
    else:
        sum += int(i)

if sum!=0:
    answer.append(str(sum))

# '' 안의 값을 구분자로 하여 리스트를 문자열로 만들기
print(''.join(answer))