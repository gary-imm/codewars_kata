#!/usr/bin/python3
#CODEWARS Kata exercise: What is between?
#https://www.codewars.com/kata/55ecd718f46fba02e5000029/train/python
#Tests Passed: 54
#Tests Failed: 0
#Instructions: Complete the function that takes two integers (a, b, where a < b)
#and return an array of all integers between the input parameters, including them.##

def between(a,b):
    empty = []
    x = range(a,b+1)
    for y in x:
        empty.append(y)
    return(empty)

#test
print(between(3,7))

#Sample Python3 Codewars solution, single line for loop
#have to return list, otherwise you will get  "range(a,b)"
def between(a,b):
    return list(x for x in range(a, b + 1))
print(between(3, 7))

#from https://blog.teamtreehouse.com/python-single-line-loops
#learning to do single line loops
def long_words(lst):
    words = []
    for word in lst:
        if len(word) > 5:
           words.append(word)
    return words

jsfk = ["sdfsdf", "sdfsdfsdf", "sdf", "Ssdfsdffsd",'ff']
print(long_words(jsfk))

##each word will be returned from [for] this list only if the length of this word is > 5
def long_words(lst):
    return [word for word in lst if len(word) > 5]
print(long_words(jsfk))
