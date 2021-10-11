"""
随机算术题，输入n（题数） s（随机种子），空格分开
"""
import logging as log
print('随机算术题，输入n（题数） s（随机种子），空格分开!')
n,s=map(int,input().split())
import random as r
r.seed(s)
grade,t,f=0,0,0
for k in range(n):
    x=r.randint(1,100)
    y=r.randint(1,100)
    sign=r.choice('+-*/')
    test=str(x)+' '+sign+' '+str(y)
    print(test+' = ?')
    ans=eval(test)
    an=eval(input())
    if ans==an:
        rt='正确'
        grade+=100/n
        t+=1
    else:
        rt='错误'
        f+=1
    print('{} = {},你的答案是{}，{}'.format(test,ans,an,rt))
print('答对{}题，答错{}题，得分{}'.format(t,f,grade))
