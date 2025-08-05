import math

prices = []
while True:
    price = input()
    if price != "":
        prices.append(price)
    else:
        break

prices = list(map(float, prices))
total = sum(prices)
print(total)
print((total * 100) % 5)

if (total * 100) % 5 == 0:
    pass

else:
    total = 5 * round(total / 5, 2)

print(total)
