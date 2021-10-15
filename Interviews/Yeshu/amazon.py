import math

def findLowestPrice(products, discounts):
    res = 0
    discountsMap = {}

    for tag, type, disc in discounts:
        discountsMap[tag] = (int(type), int(disc))

    for product in products:
        original = int(product[0])
        price = original

        for i in range(1, len(product)):
            if product[i] == "EMPTY":
                continue

            discountedPrice = original
            discount = discountsMap[product[i]]

            if discount[0] == 0: # type 0
                discountedPrice = discount[1]
            elif discount[0] == 1: # type 1
                discountedPrice = round(discountedPrice - (discountedPrice * (discount[1]/100)))
            else:
                discountedPrice = discountedPrice-discount[1]

            price = min(price, discountedPrice)

        res += price

    return res


print(findLowestPrice([['10', 'sale', 'jan-sale'], ['200', 'sale', 'EMPTY']], [['sale', '0', '10'], ['jan-sale', '1', 10]]))


# def frequency(s):
#     res = [0] * 26
#     i = 0

#     while i < len(s):
#         c, count = -1, 1
#         if i+2 < len(s) and s[i+2] == '#':
#             c = int(s[i:i+2])
#             i += 3
#         else:
#             c = int(s[i])
#             i += 1
        
#         if i < len(s) and s[i] =='(':
#             i += 1
#             cur = ''
#             while s[i] != ')':
#                 cur += s[i]
#                 i += 1
#             i += 1
#             count = int(cur)

#         res[c-1] += count
    
#     return res

# print(frequency("1226#24#"))
# print(frequency("1(12)23(3)"))
