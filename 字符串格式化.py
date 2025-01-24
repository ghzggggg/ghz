x = '{:0>6s}\t     {:s}\t    ￥{:,.2f}'
o = input('请输入商品号:')
p = input('请输入商品名:')
q = float(input('请输入商品价:'))
D={'1':'o','2':'p','3':'q'}
print(x.format(o,p,q))