s = input()
cnt = [0,0]

cnt[int(s[0])] += 1

for i in range(1,len(s)):
    if s[i] != s[i-1]:
        cnt[int(s[i])] += 1

print(min(cnt))