import os
import subprocess
import module.parameters
#对拍部分，首先编译两个代码然后运行exe再比较结果

#编译运行代码
def RunCode(
    #代码路径
    cppCode = ".\\code\\main.cpp",
    #编译器
    translater = "g++",
    #缓存路径
    tmpPath = ".\\code\\debug\\",
    #数据路径
    inpPath = ".\\data\\in\\",
    oupPath = ".\\data\\out\\",
    #数据个数
    dataNum = 10, 
    #模式
    model = "out",
):

    #执行编译
    os.system("%s %s -o %stest%s"%(translater,cppCode,tmpPath,model))
    
    #运行程序
    for i in range(1,dataNum+1):
        subprocess.call(
            "%stest%s.exe"%(tmpPath,model),
            stdin=open("%s%d.in"%(inpPath,i),"r"),
            stdout=open("%s%d.%s"%(oupPath,i,model),"w"),
            shell=True,
        )


#对输出结果比较
def CheckAns(
    #数据路径
    oupPath = ".\\data\\out\\",
    checkPath = ".\\data\\check\\",
    #数据个数
    dataNum = 10,
    #数据格式
    oupModel = "out",
    checkModel = "check",
):  

    checkLog = open("log.check","wb",buffering=0)

    for i in range(1,dataNum+1):
        j = 1
        can = True
        for line1,line2 in zip(open("%s%d.%s"%(oupPath,j,oupModel),"r"),open("%s%d.%s"%(checkPath,j,checkModel),"r")):
            if(line1!=line2):
                print("第%d组，第%d行发现错误[wa]： outAns=%s  checkAns=%s ，checkLog has saved."%(i,j,line1,line2))
                checkLog.write(("第%d组，第%d行发现错误[wa]： outAns=%s  checkAns=%s ，checkLog has saved.\n"%(i,j,line1,line2)).encode("UTF-8"))
                can = False
                break
        if(can):
            print("第%d组，未发现错误[ac]：checkLog has saved."%(i))
            checkLog.write(("第%d组，未发现错误[ac]：checkLog has saved.\n"%(i)).encode("UTF-8"))