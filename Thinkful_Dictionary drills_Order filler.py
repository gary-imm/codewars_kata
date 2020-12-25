#!/usr/bin/python3
#CODEWARS Kata exercise: Thinkful - Dictionary drills: Order filler
#https://www.codewars.com/kata/586ee462d0982081bf001f07/train/python
#Passed: 203 Tests, Failed: 0 Tests
def fillable(stock, merch, n):
    if merch in stock.keys():
        if stock.get(merch) >= n:
            print("We can complete this order")
            return True
        if stock.get(merch) < n:
            print(f"Not enough {merch} in stock. Please check again tomorrow")
            return False
    else:
        print("We do not carry this item at the moment")
        return False

item = str(input("What would you like to order?: ")).upper().strip()
unit = int(input(f"How many {item} do you want?: "))
stocky = {
    'MOVIES': 100,
    'SEASHELLS': 10,
    'BALLOONS': 1,
    'BOWLS': 5,
}
fillable(stocky, item, unit)