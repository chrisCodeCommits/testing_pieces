from collections import Counter
 
myString = input()
myCounter = Counter(myString)

for i, char in enumerate(myString):
    if myCounter[char] > 1:
        print(char)
        break
else:
    print("non")
