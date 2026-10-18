# Problem 12: Set .discard(), .remove() & .pop()
# HackerRank: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    parts = input().split()
    if parts[0] == "pop":
        s.pop()
    elif parts[0] == "remove":
        s.remove(int(parts[1]))
    else:
        s.discard(int(parts[1]))
print(sum(s))
