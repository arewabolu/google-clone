scores=2
while scores<100 and scores >-100 :
    print (scores)
    scores-=50

counter = 0
total = 0
number = 0
while number >= 0:
    number = int(input("Enter a positive number\nor a negative to exit: "))
    total += number
    counter += 1
    average = total / counter
    print(average)
else:
    print("This is a negative number")
    
text = input("Type in some words: ")
for character in text:
    print(character)
