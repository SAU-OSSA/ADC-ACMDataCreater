import module.parameters
import module.defineClass
import random
import sys
defaultPara = module.defineClass.val("defaultPara") 

#根据给定数据格式创建数据文件
def CreatInp(dateNum = 10):
    __stdoutP = sys.__stdout__
    for _ in range(1,dateNum+1):
        sys.stdout = open("%s%d.in"%(defaultPara.InpPath,_),'w')

        #定制数据输出#########################

        t = 10
        print(t)
        for i in range(t):
            print(i+3)
    
        #####################################
        sys.stdout.close()
    sys.stdout = __stdoutP
    pass