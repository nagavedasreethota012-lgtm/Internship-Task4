# Problem 19: Company Logo
# HackerRank: https://www.hackerrank.com/challenges/most-commons/problem


from collections import Counter

if __name__ == '__main__':
    s = input()

    char_count = Counter(s)

    sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))

    for char, count in sorted_chars[:3]:
        print(char, count)
