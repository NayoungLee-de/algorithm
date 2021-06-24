from itertools import combinations

n = int(input())
coin = list(map(int, input().split()))

m = [0] * (sum(coin) +1)
m[0] = 1
m[sum(coin)] = 1

for i in coin:
    m[i] = 1

for i in range(2, n):
    co = list(combinations(coin,i))
    for a in co:
        m[sum(a)] = 1

print(m.index(0))

"""
책 코드. 훨씬 간단하다
동전을 정렬한 뒤 단위가 작은 동전부터 확인하며 target 변수 update
거스름돈 문제와 달리 동전 수가 한정적임

n = int(input())
coin = list(map(int, input().split()))
coin.sort()

target = 1 # 1을 만들 수 있는지
for x in coin:
    # 만들 수 없는 금액을 찾았을 때 반복종료
    if target < x:
        break
    target += x

print(target)
"""

"""
5
3 2 1 1 9
"""