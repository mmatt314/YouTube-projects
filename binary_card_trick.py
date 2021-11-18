no_of_cards = input("How many cards would you like to use?\n")

card_1 = []
card_2 = []
card_3 = []
card_4 = []
card_5 = []
card_6 = []
card_7 = []
card_8 = []
card_9 = []
card_10 = []

max_number = 2 ** int(no_of_cards) # don't have to take 1 away since the range function'll do it in the next step!
for x in range(1, max_number):
    y = x
    if x >= 512:
        card_10.append(y)
        x -= 512
    if x >= 256:
        card_9.append(y)
        x -= 256
    if x >= 128:
        card_8.append(y)
        x -= 128
    if x >= 64:
        card_7.append(y)
        x -= 64
    if x >= 32:
        card_6.append(y)
        x -= 32
    if x >= 16:
        card_5.append(y)
        x -= 16
    if x >= 8:
        card_4.append(y)
        x -= 8
    if x >= 4:
        card_3.append(y)
        x -= 4
    if x >= 2:
        card_2.append(y)
        x -= 2
    if x >= 1:
        card_1.append(y)

print(card_10)
print(card_9)
print(card_8)
print(card_7)
print(card_6)
print(card_5)
print(card_4)
print(card_3)
print(card_2)
print(card_1)


