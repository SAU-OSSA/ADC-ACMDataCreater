import module.parameters
import module.defineClass
import random
import sys
from copy import deepcopy
import cyaron

defaultPara = module.defineClass.val("defaultPara") 

#根据给定数据格式创建数据文件
def CreatInp(dateNum = module.defineClass.val("defaultPara").DataNum):
    __stdoutP = sys.__stdout__
    for ___ in range(1,dateNum+1):
        sys.stdout = open("%s%d.in"%(defaultPara.InpPath,___),'w')
        #__stdoutP.write("第%d项开始输出："%(___))
        #定制数据输出#########################

        t = 1#rdt(1,10)
        #print(t)
        for _ in range(t):
            n = rdt(1,1000)
            print(n)
            #prf(rdt(1,10,n))
            ct = 0
            mp = {x:0 for x in range(11)}
            a = list()
            while(ct < n):
                if(len(a)>0 and rdt(0,1)==1):
                    print(a[-1],end=' ')
                    mp[a[-1]]-=1
                    a.pop(-1)
                    ct += 1
                else:
                    s = set()
                    for i in mp:
                        if(mp[i]==0):
                            s.add(i)
                    if(len(s)==0): continue
                    x = rdt(0, 10)
                    while x not in s: x = rdt(0,10)
                    a.append(x)
                    print(x,end=' ')
                    mp[x]+=1
                    ct += 1
            print(' ')


#       https://github.com/luogu-dev/cyaron/wiki/%E5%9B%BE-Graph
#
#       n = rdt(10000,20000)
#       m = rdt(20000,100000)
#       k = 0
#        
#       graph = cyaron.Graph.graph(n,m,weight_limit=(0,6),self_loop=False, repeated_edges=False);
#       es = []
#       for edge in graph.iterate_edges():
#           v = edge.start;
#           u = edge.end;
#           c = edge.weight;
#           if(c==1 and k<n-1):
#               k+=1
#           else:
#               c=0
#           es.append([v,u,c])
#
#       k = rdt(k//5,k)
#       print(n,m,k)
#       for e in es:
#           prf(e)
#
        #####################################
        sys.stdout.close()
    sys.stdout = __stdoutP
    pass

def rdt(a,b,num = 0):
    a = int(a);b = int(b);num = int(num)
    if num==0:
        return random.randint(a,b)
    else:
        return [ random.randint(a,b) for i in range(num)]

def rdtf(a,b,ws = 3,num = 0):
    num = int(num)
    wsp = pow(10,ws)
    a = a*wsp
    b = b*wsp
    if num==0:
        return random.randint(a,b)/wsp
    else:
        return [ random.randint(a,b)/wsp for i in range(num)]


def prf(arr,spt=" ",endl="\n"):
    for ai in arr:
        print(ai,end=spt)
    print(endl,end="")

