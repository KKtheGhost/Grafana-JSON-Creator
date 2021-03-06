#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Date    : 2018-09-10 16:43:06
#@Author  : Kivinsae Fang (fangwei@xindong.com)
#@QQ      : 1669815117
#@Version : 0.3.3

import os
import math
import shutil

## [Delet&Create files]每次使用前清理上一次使用残留的file1和file3文件。
def DelCrtFile():
    os.remove('./file1')
    os.remove('./file3')
    os.mknod('./file1')
    os.mknod('./file3')

#[Read&Write]读取预设文档并把内容写入file1
def RdWrt():
    ifn = "./beijing-n7k-ethernet"             ##此处填写利用的模板json文件
    ofn = "./file1"
    infile = open(ifn, 'r')
    outfile = open(ofn, 'w')
    outfile.write(infile.read())
    infile.close()
    outfile.close()

def CrtWrt2():
    shutil.copyfile("./file1","./file2")               ##直接复制一个和file1一样的源文件。用来后面做循环。

## [Delete file 2]用来删除file2从而进行下一个循环
def DelF2():
    os.remove('./file2')

## [Switch ServerName]这个模块直接替换任何文件里面的服务器名称内容,这个函数会在循环中被反复使用
def SwhFuckingNum(i):
    with open('./file2','r+') as d1:
        infos=d1.readlines()
        d1.seek(0,0)
        d1.truncate()                   ## 灵魂语句，彻底终结尾部奇怪字符的问题。文件内容进入缓存，清空文件重写，问题解决。
        for line in infos:
            ## 下面的部分就是用来替换相关的内容的，尤其是内容和循环数有关的时候。可以自由替换。
            yaxe = (i-1)*6
            line=line.replace('thefuckingport',str(i))
            line=line.replace('yaxevar',str(yaxe))
            line=line.replace('idvariable0',str(yaxe+2))
            line=line.replace('idvariable1',str(yaxe+3))
            d1.write(line)
        d1.close()


## 把每个循环内file2的内容累加输出到file3中，作为输出结果JSON的一部分
def ToJSON():
    ifn = "./file2"
    ofn = "./file3"
    infile = open(ifn, 'r')
    outfile = open(ofn, 'a')            ##　累加写入模式
    outfile.write(infile.read())
    infile.close()
    outfile.close()

def MainF():
    i = 1
    DelCrtFile()
    RdWrt()
    while i <= 48:
        CrtWrt2()
        SwhFuckingNum(i)
        ToJSON()
        DelF2()
        i = i+1

MainF()         ##主函数运行进行JSON生成。
