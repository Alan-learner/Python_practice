"""
输入：随机数种子（s）,比赛场次（z）
输出：两个赌徒的胜率
"""
import random as r
s,z=map(int,input().split(','))
r.seed(s)
def play(x,y,n):
    if r.random()<0.5:
        x+=10
        y-=10
    else:
        x-=20
        y+=20
    n-=1
    return x,y,n
a,b,c=0,0,0
for k in range(z):
    x,y,t=100,100,z
    while x>0 and y>0:
        x,y,t=play(x,y,t)
    if x<=0:
        a+=1
    elif y<=0:
        b+=1
    elif n<=0:
        c+=1
print('A输光的概率为：{:.2f}%'.format(100*a/z))
print('B输光的概率为：{:.2f}%'.format(100*b/z))
