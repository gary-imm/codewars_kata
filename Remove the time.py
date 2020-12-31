#!/usr/bin/python3
#CODEWARS Kata exercise: Remove the time
#https://www.codewars.com/kata/56b0ff16d4aa33e5bb00008e/train/python
#Tests passed: 45
#Tests failed:0
#Pretty simple, just have to split by the comma, and the [0] lists before the comma

def shorten_to_date(long_date):
    return long_date.rsplit(",")[0]

date = "Tuesday May 5, 8PM"
print(shorten_to_date(date))