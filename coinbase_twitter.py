string = ("Inbound transfers for MATIC, SKL and SUSHI are now available in the regions where trading is supported. Traders cannot place orders and no orders will be filled. Trading will begin on or after 9AM PT on Thursday March 11 , if liquidity conditions are met.")
coins = []
c = string.replace('PT', '')
b = c.replace(',', '')
a = b.split()

for word in a:
    if word.isupper() and word.isalpha():
        coins.append(word)

print(a)
print(coins)
