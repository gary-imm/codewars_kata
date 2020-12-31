#!/usr/bin/python3
#CODEWARS Kata exercise: Unfinished Loop - Bug Fixing #1
#https://www.codewars.com/kata/55c28f7304e3eaebef0000da/train/python
#Tests Passed: 50
#Tests Failed: 0

#Instructions: Oh no, Timmy's created an infinite loop! Help Timmy find and fix the bug in his unfinished for loop!

def create_array(n):
    res=[]
    i=1
    while i<=n:
        res+=[i]
        i+=1
        if i == n+1:
            break
    return res
#Example
print(create_array(14))