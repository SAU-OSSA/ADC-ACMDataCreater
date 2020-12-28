import os
import subprocess
import module.parameters
import module.defineClass
defaultPara = module.defineClass.val("defaultPara")

#对拍部分，首先编译两个代码然后运行exe再比较结果

#编译运行代码
def RunCode(
    #代码路径
    Code =  defaultPara.Code,
    #缓存路径
    tmpPath = defaultPara.TmpPath,
    #数据路径
    inpPath = defaultPara.InpPath,
    oupPath = defaultPara.OupPath,
    #数据个数
    dataNum = defaultPara.DataNum, 
    #模式
    model = defaultPara.OupModel,
):

    #C++
    if(Code[-4:]=='.cpp'):
        #执行编译
        os.system("g++ %s -o %stest%s"%(Code,tmpPath,model))
        
        #运行程序
        for i in range(1,dataNum+1):
            subprocess.call(
                "%stest%s.exe"%(tmpPath,model),
                stdin=open("%s%d.in"%(inpPath,i),"r"),
                stdout=open("%s%d.%s"%(oupPath,i,model),"w"),
                shell=True,
            )
    elif(Code[-3:]=='.py'):
        #直接运行代码
        for i in range(1,dataNum+1):
            subprocess.call(
                'python '+Code,
                stdin=open("%s%d.in"%(inpPath,i),"r"),
                stdout=open("%s%d.%s"%(oupPath,i,model),"w"),
                shell=True,
            )


#对输出结果比较
def CheckAns(
    #数据路径
    oupPath = defaultPara.OupPath,
    checkPath = defaultPara.CheckPath,
    #数据个数
    dataNum = defaultPara.DataNum,
    #数据格式
    oupModel = defaultPara.OupModel,
    checkModel = defaultPara.Check2Model,
):  

    checkLog = open("log.check","wb",buffering=0)

    for i in range(1,dataNum+1):
        j = 1
        can = True
        for line1,line2 in zip(open("%s%d.%s"%(oupPath,i,oupModel),"r"),open("%s%d.%s"%(checkPath,i,checkModel),"r")):
            if(line1!=line2):
                print("第%d组，第%d行发现错误[wa]：\n outAns=\t%s checkAns=\t%s ,checkLog has saved."%(i,j,line1,line2))
                checkLog.write(("第%d组，第%d行发现错误[wa]：\n outAns=%s checkAns=%s ,checkLog has saved.\n"%(i,j,line1,line2)).encode("UTF-8"))
                can = False
                break
            j+=1;
        if(can):
            print("第%d组，未发现错误[ac]：checkLog has saved."%(i))
            checkLog.write(("第%d组，未发现错误[ac]：checkLog has saved.\n"%(i)).encode("UTF-8"))