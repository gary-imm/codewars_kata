#!/usr/bin/python3
#CODEWARS Kata exercise: Greek Sort
#https://www.codewars.com/kata/56bc1acf66a2abc891000561/train/python
#Passed: 503 Tests
#Failed: 0 Tests

greek_alphabet = (
    'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta',
    'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu',
    'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma',
    'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega')

def greek_comparator(lhs, rhs):
    lhs = int(greek_alphabet.index(lhs))
    rhs = int(greek_alphabet.index(rhs))
    return(lhs-rhs)

first_number = str(input("Greek alphabet letter: ")).strip().lower()
second_number = str(input("Another Greek alphabet letter: ")).strip().lower()

if first_number and second_number in greek_alphabet:
    greek_comparator(first_number, second_number)
else:
    print("Incorrect input")