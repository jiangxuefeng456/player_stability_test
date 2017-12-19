#encoding:utf-8
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

r1 = mlab.csv2rec('C:/Users/jiangxuefeng/Desktop/powers/ali360power.csv')

#绘图
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.plot(r1['360power'],label="360")
ax1.plot(r1['alipower'],label="ali")
ax1.legend(ncol=2,loc=0)
ax1.set_title(u"power")


plt.show()

