a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = int(input())
for _ in range(n):
    q = tuple(input().split())
    if(q[0]=="pop"):
        a.pop()