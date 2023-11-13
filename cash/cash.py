# TODO
while True:
    dollars = float(input("Change owed: "))
    if dollars > 0:
        break

cents = int((dollars*100) + 0.5)
total = 0
for coins in [25, 10, 5, 1]:
    total += cents // coins
    cents %= coins
    
print(total)
