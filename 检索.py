x = input("请输入您的身份证号码：")
A = list(x)
for index,item in enumerate(A):
    if index == 0:
        y=item
    if index == 1:
        z=item
w = (y+z)
print(w)
D={'62':'陕西',}
for key,value in D.items():
    if key == w:
        print('您的省份为',value)