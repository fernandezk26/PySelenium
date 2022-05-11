#simple example 1
assets = ["house", "bike", "car", "boat"]

for asset in assets:
    print(asset)
    print('--------------------------------')

fruits = ["apple", "orange", "banana"]

for fruit in fruits:
    print(fruit)

print('-------------------------------')

#example 2
#print out words that are 3 or less characters
quote = "Life doesn't get any better, you do."
small_words = []
for word in quote.split():
    if len(word) <= 3:
        small_words.append(word)
print(small_words)