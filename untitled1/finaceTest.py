# coding:utf-8
import numpy as np
# 计算终值
print("Future value",np.fv(0.03/4,5*4,-10,-1000))
fvals = []
for i in range(1,6):
    fvals.append(np.fv(0.03/4,i*4,-10,-1000))
    print('first',i,fvals[i-1])
# 现值
print("Present value",np.pv(0.03/4,5*4,-10,fvals[4]))
# 净现值
print('npv',np.npv(0.281,[-100,39,59,55,20]))
# pmt函数
print('每月需还贷的金额为',np.pmt(0.075/12,12*15,200000))

# 房贷20万，年利率7.5%,每月能还贷2000,则需要还多少期
# nper函数
print('需还贷:',np.ceil(np.ceil(np.nper(0.075/12,-2000,200000))/12),'个月')

print('需还贷')
month=np.nper(0.075/12,-2000,200000)
print(month)
print(np.ceil(np.ceil(month)/12))
print('年')

# 房贷20万，需还14年，每月还2000，年利率多少
print("Interest rate",12*np.rate(month,-2000,200000,0))

print('每月需还贷的金额为',np.pmt(0.06/12,12*20,1400000))
