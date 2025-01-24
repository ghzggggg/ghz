n,m = map(int,input().split())
label_price = []
for _ in range(n):
    li = input().split()
    price_purchase = {}
    for s in li:
        a,b = map(int,s.split(":"))
        price_purchase[a] = b
    label_price.append(price_purchase)
discount = []
for _ in range(m):
    li = input().split()
    brand= []
    for s in li:
        level,cut = map(int,s.split("-"))
        brand.append((level,cut))
    discount.append(brand)
each_purchase = [0]*m
for each_one in label_price:
    for each_brand in each_one.keys():
        each_purchase[each_brand-1] += each_one[each_brand]
dis1 = 50*(sum(each_purchase)//300)
dis2 = 0
for brand in range(m):
    every_discount = 0
    for level,cut in discount[brand]:
        if each_purchase[brand] >= level:
            every_discount = cut
    dis2+=every_discount
final_cost = sum(each_purchase)-dis1-dis2
print(final_cost)