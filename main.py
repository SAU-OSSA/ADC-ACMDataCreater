import module.createDate as createDate
import module.checkMain as checkMain
import module.defineClass as defineClass
import argparse
import os
defaultPara = defineClass.val("defaultPara")

# 第一次启动初始化必备目录结构


def Mkdir(path):
    if os.path.exists(path):
        return
    else:
        os.makedirs(path)


Mkdir("./data/check")
Mkdir("./data/testData")
#Mkdir("./data/out")
Mkdir("./code/debug")

Main = argparse.ArgumentParser(description="数据生成&对拍器")
Main.add_argument(
    '-m', '--model',
    help='应用启动模式\t0新随机数据为标程数据生成,\t1以原数据为标程数据生成,\t2用标准数据为程序对拍,\t3为重新计算标准数据并对拍',
    type=int,
    choices=[0, 1, 2, 3],
)

Main.add_argument(
    '-p1', '--path1',
    help='标程位置',
    type=str,
)
Main.add_argument(
    '-p2', '--path2',
    help='测程位置',
    type=str,
)

args = Main.parse_args()


if(args.model == 0):
    print("数据生成...")
    createDate.CreatInp()
    if(args.path1 == None or not os.path.exists(args.path1)):
        print("未输入标程路径或路径错误采用默认路径")
        checkMain.RunCode()
    else:
        print("正在为指定标程生成数据")
        checkMain.RunCode(Code=args.path1)
    print("完成")

elif(args.model == 1):
    print("以原数据生成标程数据...")
    if(args.path1 == None or not os.path.exists(args.path1)):
        print("未输入标程路径或路径错误采用默认路径")
        checkMain.RunCode()
    else:
        print("正在为指定标程生成数据")
        checkMain.RunCode(Code=args.path1)
    print("完成")

elif(args.model == 2):
    print("用标准数据对拍...")
    if(args.path2 == None or not os.path.exists(args.path2)):
        print("未输入测试代码路径或位置出错采用默认路径")
        checkMain.RunCode(Code=defaultPara.Check2Code,
                          oupPath=defaultPara.CheckPath, model=defaultPara.Check2Model)
    else:
        print("正在为指定代码对拍")
        checkMain.RunCode(
            Code=args.path2, oupPath=defaultPara.CheckPath, model=defaultPara.Check2Model)
    checkMain.CheckAns()
    print("完成")

elif(args.model == 3):
    print("用指定代码生成数据对拍...")
    if(args.path1 == None or not os.path.exists(args.path1)):
        print("未输入对拍代码1路径或路径错误采用默认路径")
        checkMain.RunCode(Code=defaultPara.Check1Code,
                          oupPath=defaultPara.CheckPath, model=defaultPara.Check1Model)
    else:
        print("正在运行对拍代码1")
        checkMain.RunCode(
            Code=args.path1, oupPath=defaultPara.CheckPath, model=defaultPara.Check1Model)
    if(args.path2 == None or not os.path.exists(args.path2)):
        print("未输入对拍代码2路径或路径错误采用默认路径")
        checkMain.RunCode(Code=defaultPara.Check2Code,
                          oupPath=defaultPara.CheckPath, model=defaultPara.Check2Model)
    else:
        print("正在运行对拍代码2")
        checkMain.RunCode(
            Code=args.path2, oupPath=defaultPara.CheckPath, model=defaultPara.Check2Model)
    checkMain.CheckAns(
        oupPath=defaultPara.CheckPath, oupModel=defaultPara.Check1Model,
        checkPath=defaultPara.CheckPath, checkModel=defaultPara.Check2Model)

    print("完成")
