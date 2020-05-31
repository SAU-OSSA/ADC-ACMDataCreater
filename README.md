# 对拍器

用于算法竞赛选手代码对拍或大量随机数据生成，目前仅支持C++代码。



## 文档目录

[TOC]

## 快速开始

##### 运行环境

*   python 3.6+
*   g++ 6.3.0+

##### 克隆代码库

```cmd
git clone git@github.com:SAU-OSSA/ADC-ACMDateCreater.git
```

##### 安装运行库

```cmd
pip install argparse
pip install subprocess
```



## 使用说明

在代码根目录下运行 `./main.py -h` 可以查看简要命令说明，并初始化目录结构。

除此之一共有4种运行模式。



##### 以现有数据和给定标程生成输出

```cmd
./main -m 0 -p1 标程位置
```

需要在 `./data/in` 下防止10 组输入输出，命名格式为 x.in，$x\in[1,10]$ 。

随后会以指定标程运行，并将输出存入 `./data/out` 文件夹下。

*参数 `p1` 可以省略，将采用默认位置 `./code/main.cpp`



##### 以随机数据和给定标程生成输出

```cmd
./main -m 1 -p1 标程位置
```

不需要手动导入输入文件。程序将在执行后根据 `./module/creatDate.py` 的输出生成 10 组随机数据。

可以通过修改 `creatDate.py` 的内容改变数据生成。

再以指定标程运行，结果输出位置与上一个命令相同。

*参数 `p1` 可以省略，将采用默认位置 `./code/main.cpp`



##### 以给定标程输入输出和现有程序对拍

```cmd
./main -m 2 -p2 测试程序位置
```

需要保证已经运行过上两个命令，或者在输入文件夹和输出文件夹下有 10 组标程的输入输出数据。

此命令将运行测试程序，并将输出结果存入 `./data/check` 目录下。

随后用测试输出结果与标程输出逐行对比。

*参数 `p2` 可以省略，将采用默认位置 `./code/check2.cpp`



##### 对拍两个测试程序

```cmd
./main -m 3 -p1 测试程序1位置 -p2 测试程序2位置
```

确保输入文件目录下文件健全。

此命令将依次运行两个测试程序，并将输出结果存入 `./data/check` 目录下。

随后逐行对比两组输出结果。

*参数 `p1` 可以省略，将采用默认位置 `./code/check1.cpp`

*参数 `p2` 可以省略，将采用默认位置 `./code/check2.cpp`



## 开源协议

[AGPLv3.0](https://github.com/SAU-OSSA/ADC-ACMDateCreater/blob/master/LICENSE) 协议。
