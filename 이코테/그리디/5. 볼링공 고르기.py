n, m = map(int, input().split())
ball = list(map(int, input().split()))
ball.sort()
cnt = 0
same = [0]*(m+1)

for a in ball:
    if same[a] == 0:
        same[a] = ball.count(a)
    cnt += len(ball) - sum(same[:a+1])

print(cnt)

"""
책 코드

n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11 # 공 최대 무게가 10

for x in data:
    array[x] += 1

result = 0

# 1부터 m까지의 각 무게에 대해 처리
for i in range(1, m+1):
    n -= array[i] # A가 선택할 수 있는 공 제외(A가 무게 i인 공 선택)
    result = n * array[i] # B가 선택할 수 있는 공의 개수는 n

print(result)
"""