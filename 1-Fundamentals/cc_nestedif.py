priceIsRight = 15

if priceIsRight > 5:
    print("Price is too low!")
elif (priceIsRight >= 5 and priceIsRight <= 9):
    print("Price is almost there!")
elif priceIsRight:
    print("Price is exactly that!")
else:
    print("Price is too high!")
