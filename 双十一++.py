result = float('inf')
n,m = map(int,input().split())
label_price = [input().split() for _ in range(n)]
discount = [input().split() for _ in range(m)]

def cost_plan(label_price,discount,each_one=0,total=0,each_purchase =[0]*m ):
    global result
    if each_one == n:
        cut = 0
        for brand in range(m):
            each_cut = 0
            for s in discount[brand]:
                level,diss = map(int,s.split('-'))
                if each_purchase[brand] >= level:
                    each_cut = max(each_cut,diss)
            cut+=each_cut
        result = min(result,total-50*(total//300)-cut)
        return

    for i in label_price[each_one]:
        a,each_price = map(int,i.split(':'))
        each_purchase[a-1] += each_price
        cost_plan(label_price,discount,each_one+1,total+each_price,each_purchase)
        each_purchase[a-1] -= each_price

cost_plan(label_price,discount)
print(result)