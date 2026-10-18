# Problem 9: What's Your Name?
# HackerRank: https://www.hackerrank.com/challenges/whats-your-name/problem

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

first = input().strip()
last = input().strip()
print_full_name(first, last)
