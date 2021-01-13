#!/usr/bin/python3
#CODEWARS Kata exercise: Sum of positive
#https://www.codewars.com/kata/5715eaedb436cf5606000381/train/python
#Tests Passed: 45
#Tests Failed: 0
#Instructions: You get an array of numbers, return the sum of all of the positives ones.

#I attempted this both with multiple line and single line loops

def positive_sum(arr):
    sum = 0
    for num in arr:
        if num >= 0:
            sum += num
    return sum

list = (3, 5, 1, 5)
print(positive_sum(list))

def positive_sum(arr):
    total = [x for x in arr if x >= 0]
    return sum(total)

list = (2, 7, -26, 6)
print(positive_sum(list))