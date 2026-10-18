# Problem 20: Validating the Phone Number
# HackerRank: https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re
for _ in range(int(input())):
    number = input().strip()
    print("YES" if re.fullmatch(r"[789]\d{9}", number) else "NO")
