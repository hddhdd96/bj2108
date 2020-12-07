import sys

from collections import Counter

N = int(sys.stdin.readline())

N_list = []

for i in range(N):
    N_list.append(int(sys.stdin.readline()))

N_list.sort()

# 1
print(round(sum(N_list)/N))

# 2
print(N_list[N//2])

# 3
AN_list = Counter(N_list).most_common()

if len(AN_list) > 1:
    if AN_list[0][1] == AN_list[1][1]:
        print(AN_list[1][0])
    else:
        print(AN_list[0][0])
else:
    print(AN_list[0][0])


# 4
print(N_list[-1] - N_list[0])
