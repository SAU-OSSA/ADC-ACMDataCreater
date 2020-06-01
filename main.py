import module.createDate as createDate
import module.checkMain as checkMain
import argparse
import os


#第一次启动初始化必备目录结构
def Mkdir(path):
    if os.path.exists(path):
        return
    else:
        os.makedirs(path)

Mkdir("./data/check")
Mkdir("./data/in")
Mkdir("./data/out")
Mkdir("./code/debug")

Main = argparse.ArgumentParser(description="数据生成&对拍器")
Main.add_argument(
    '-m','--model', 
    help='应用启动模式\t0以原数据为标程数据生成,\t1新随机数据为标程数据生成,\t2用标准数据为程序对拍,\t3为重新计算标准数据并对拍',
    type = int,
    choices = [0,1,2,3],
)
Main.add_argument(
    '-p1','--path1', 
    help='标程位置',
    type = str,
)
Main.add_argument(
    '-p2','--path2', 
    help='测程位置',
    type = str,
)

args = Main.parse_args()


if(args.model==0):
    print("数据生成...")
    createDate.CreatInp()
    if(args.path1==None or not os.path.exists(args.path1)):
        print("未输入标程路径或路径错误采用默认路径")
        checkMain.RunCode()
    else:
        print("正在为指定标程生成数据")
        checkMain.RunCode(cppCode=args.path1)
    print("完成")

elif(args.model==1):
    print("以原数据生成标程数据...")
    if(args.path1==None or not os.path.exists(args.path1)):
        print("未输入标程路径或路径错误采用默认路径")
        checkMain.RunCode()
    else:
        print("正在为指定标程生成数据")
        checkMain.RunCode(cppCode=args.path1)
    print("完成")

elif(args.model==2):
    print("用标准数据对拍...")
    if(args.path2==None or not os.path.exists(args.path2)):
        print("未输入测试代码路径或位置出错采用默认路径")
        checkMain.RunCode(cppCode=".\\code\\check2.cpp",oupPath=".\\data\\check\\",model='check2')
    else:
        print("正在为指定代码对拍")
        checkMain.RunCode(cppCode=args.path2,oupPath=".\\data\\check\\",model='check2')
    checkMain.CheckAns(checkPath=".\\data\\check\\",checkModel='check2')
    print("完成")

elif(args.model==3):
    print("用指定代码生成数据对拍...")
    if(args.path1==None or not os.path.exists(args.path1)):
        print("未输入对拍代码1路径或路径错误采用默认路径")
        checkMain.RunCode(cppCode=".\\code\\check1.cpp",oupPath=".\\data\\check\\",model='check1')
    else:
        print("正在运行对拍代码1")
        checkMain.RunCode(cppCode=args.path1,oupPath=".\\data\\check\\",model='check1')
    if(args.path2==None or not os.path.exists(args.path2)):
        print("未输入对拍代码2路径或路径错误采用默认路径")
        checkMain.RunCode(cppCode=".\\code\\check2.cpp",oupPath=".\\data\\check\\",model='check2')
    else:
        print("正在运行对拍代码2")
        checkMain.RunCode(cppCode=args.path2,oupPath=".\\data\\check\\",model='check2')
    checkMain.CheckAns(
        oupPath = ".\\data\\check\\",oupModel="check1",
        checkPath=".\\data\\check\\",checkModel='check2'
    )
    print("完成")
    