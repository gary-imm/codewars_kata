#!/usr/bin/python3
#CODEWARS Kata exercise: Squash the bugs
#https://www.codewars.com/kata/56f173a35b91399a05000cb7/train/python
#Tests Passed: 45
#Tests Failed: 0

def find_longest(string):
    spl = string.split(" ")
    longest = 0
    for i in spl:
        if len(i) > longest:
            longest = int(len(i))
    return longest

bring = str(input("Type a sentence: "))
print(find_longest(bring))