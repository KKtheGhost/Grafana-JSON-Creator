#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Date    : 2018-09-10 16:43:06
#@Author  : Kivinsae Fang (fangwei@xindong.com)
#@QQ      : 1669815117
#@Version : 0.3.3

import os
import math

## [Delet&Create files]每次使用前清理上一次使用残留的file1和file3文件。
def DelCrtFile():
    os.remove('./file1')
    os.remove('./file3')
    os.mknod('./file1')
    os.mknod('./file3')

#[Read&Write]读取预设文档并把内容写入file1，读取哪个根据输入变量FuncP决定
def RdWrt():
    ifn = "./ECS-ALL-Module"
    ofn = "./file1"
    infile = open(ifn, 'r')
    outfile = open(ofn, 'w')
    outfile.write(infile.read())
    infile.close()
    outfile.close()

## [Create&Write file2]生成中转文件File2并把file1的内容写入。这个函数会在循环中被反复使用
def CrtWrt2():
    os.mknod('./file2')
    ifn = r"./file1"
    ofn = r"./file2"
    infile = open(ifn, 'r')
    outfile = open(ofn, 'w')
    outfile.write(infile.read())
    infile.close()
    outfile.close()

## [Delete file 2]用来删除file2从而进行下一个循环
def DelF2():
    os.remove('./file2')

## [Switch ServerName]这个模块直接替换任何文件里面的服务器名称内容,这个函数会在循环中被反复使用
def SwhSvr(SvrName):
    with open('./file2','r+') as d1:
        infos=d1.readlines()
        d1.seek(0,0)
        for line in infos:
            line_new1=line.replace('SlbName',SvrName)
            d1.write(line_new1)
        d1.close()

def SwhNmbNet(NmbNet):
    with open('./file2','r+') as d1:
        infos=d1.readlines()
        d1.seek(0,0)
        for line in infos:
            line_new1=line.replace('NumberNet',NmbNet)
            d1.write(line_new1)
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

## 因能力所限，在每个循环的尾部出现了迷之额外括号，所以设置字符删减函数。并且在原模函数的尾部添加7-8换行符
def EditTail():
    f = open("./file2","rb+")
    f.seek(-5,os.SEEK_END)
    f.truncate()
    f.close()

## 获取需要内容。主要是服务器名头，服务器数量，需要生成的模块。
NodeNum=int(raw_input("一共有多少台服务器:"))                        ## 服务器数量Node Number

## 服务器尾缀可以根据项目自行调整
XdID=".xd.cn"

## 节省一下行数
def MainF(i):
    j=i-1
    file = open('./slb')
    SvrName=file.readlines()[j]
    SvrName=SvrName.strip('\n')
    SwhSvr(SvrName)
    SwhNmbNet(NmbNet)
    EditTail()
    ToJSON()
    DelF2()

## [Main]主函数，在循环中不断往file3中输出的循环语句
if __name__ == '__main__':
    i = 1
    DelCrtFile()
    RdWrt()
    while i <= NodeNum:
        if i < 71:                          ## 防止服务器数量小于10时发生错误
            CrtWrt2()
            NmbNet='unet'+str(170-i)
            MainF(i)
            i = i+1
        elif i >=71:
            CrtWrt2()
            NmbNet='unet0'+str(170-i)
            MainF(i)
            i = i+1
        else:
            print "JSON输出完毕，请查看通文件夹下的file3"
