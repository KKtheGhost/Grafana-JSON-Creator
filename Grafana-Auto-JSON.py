#!/usr/bin/env python
#-*- coding: utf-8 -*-
#@Date    : 2018-09-10 16:43:06
#@Author  : Kivinsae Fang (fangwei@xindong.com)
#@QQ      : 1669815117
#@Version : 0.3.3

import os
import math

print "本脚本适用于安装且运行了InfluxDB+telegraf监控套件的系统。"
print "本脚本默认机器使用了telegraf默认基础硬件监控配置。"
print "使用完本脚本后请cat文件夹中的file1来查看需要的代码，并且粘贴到对应dashboard中的panel当中去。"

## [Delet&Create files]每次使用前清理上一次使用残留的file1和file3文件。
def DelCrtFile():
    os.remove('./file1')
    os.remove('./file3')
    os.mknod('./file1')
    os.mknod('./file3')

#[Read&Write]读取预设文档并把内容写入file1，读取哪个根据输入变量FuncP决定
def RdWrt():
    ifn = "./"+FuncP+"-module-"+GmID
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
            line_new1=line.replace('SvrNm',SvrName)
            d1.write(line_new1)
        d1.close()

## [Switch Location X]这个模块用来替换Panel位置的X坐标,这个函数会在循环中被反复使用
def SwhLctX(i):
    with open('./file2','r+') as d1:
        x = ((i-1)%3)*8
        infos=d1.readlines()
        d1.seek(0,0)
        for line in infos:
            line_new1=line.replace('Xlocate',str(x))
            d1.write(line_new1)
        d1.close()

## [Switch Location Y]这个模块用来替换Panel位置的Y坐标,这个函数会在循环中被反复使用
def SwhLctY(i):
    with open('./file2','r+') as d2:
        y = ((i-1)//3)*9
        sofni=d2.readlines()
        d2.seek(0,0)
        for line in sofni:
            line_new1=line.replace('Ylocate',str(y))
            d2.write(line_new1)
        d2.close()

## [Switch ID]这个模块用来替换Panel的ID,这个函数会在循环中被反复使用
def SwhID(i):
    with open('./file2','r+') as d3:
        sofni=d3.readlines()
        d3.seek(0,0)
        for line in sofni:
            line_new1=line.replace('PanelID',str(i+1))
            d3.write(line_new1)
        d3.close()

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
    f.seek(-21,os.SEEK_END)
    f.truncate()
    f.close()

## 获取需要内容。主要是服务器名头，服务器数量，需要生成的模块。
GmID=raw_input("是哪个项目(例如横扫千军，就是「46x」):")          ## 游戏名头GameID
NodeNum=int(raw_input("一共有多少台服务器:"))                        ## 服务器数量Node Number
FuncP=raw_input("需要生成哪个模块(CPU|DB|Load|Mem|Net):")       ## Function Pick 选择功能

## 节省一下行数创造一个功能性MainF主函数
def MainF(i):
    SwhLctX(i)
    SwhLctY(i)
    SwhID(i)
    EditTail()
    ToJSON()
    DelF2()

## 横扫千军项目函数
def hengsao(GmID):
    i = 1
    XdID=".xd.cn"
    DelCrtFile()
    RdWrt()
    while i <= NodeNum:
        if i < 10:                          ## 防止服务器数量小于10时发生错误
            CrtWrt2()
            SvrName=(GmID+'00'+str(i)+XdID)
            SwhSvr(SvrName)
            MainF(i)
            i = i+1
        elif 10 <= i and i < 100:
            CrtWrt2()
            SvrName=(GmID+'0'+str(i)+XdID)
            SwhSvr(SvrName)
            MainF(i)
            i = i+1
        elif i >= 100:
            CrtWrt2()
            SvrName=(GmID+str(i)+XdID)
            SwhSvr(SvrName)
            MainF(i)
            i = i+1
        else:
            print "搞毛啊几万台服务器兄弟？"

## 仙境传说项目函数
def RO(GmID):
    i = 1
    XdID=".xd.cn"
    DelCrtFile()
    RdWrt()
    while i <= NodeNum:
        if i < 10:                          ## 防止服务器数量小于10时发生错误
            CrtWrt2()
            SvrName=(GmID+'00'+str(i)+XdID)
            SwhSvr(SvrName)
            MainF(i)
            i = i+1
        elif 10 <= i < 100:
            CrtWrt2()
            SvrName=(GmID+'0'+str(i)+XdID)
            SwhSvr(SvrName)
            MainF(i)
            i = i+1
        elif i >= 100:
            CrtWrt2()
            SvrName=(GmID+str(i)+XdID)
            SwhSvr(SvrName)
            MainF(i)
            i = i+1
        else:
            print "搞毛啊几万台服务器兄弟？"

## 仙侠道1项目函数
def XXD1(GmID):
    i = 1
    XdID=".xd.com"
    DelCrtFile()
    RdWrt()
    while i <= NodeNum:
        if i < 10:                          ## 防止服务器数量小于10时发生错误
            CrtWrt2()
            SvrName=(GmID+'0'+str(i)+XdID)
            SwhSvr(SvrName)
            MainF(i)
            i = i+1
        elif i >= 10:
            CrtWrt2()
            SvrName=(GmID+str(i)+XdID)
            SwhSvr(SvrName)
            MainF(i)
            i = i+1
        else:
            print "搞毛啊几万台服务器兄弟？"

## 仙侠道2项目函数
def XXD2(GmID):
    i = 1
    XdID=".xd.com"
    DelCrtFile()
    RdWrt()
    while i <= NodeNum:
        if i < 10:                          ## 防止服务器数量小于10时发生错误
            CrtWrt2()
            SvrName=(GmID+'0'+str(i)+XdID)
            SwhSvr(SvrName)
            MainF(i)
            i = i+1
        elif i >= 10:
            CrtWrt2()
            SvrName=(GmID+str(i)+XdID)
            SwhSvr(SvrName)
            MainF(i)
            i = i+1
        else:
            print "搞毛啊几万台服务器兄弟？"

## 用来添加不同的项目函数
def runJSON(GmID):
        if GmID == '46x':
            hengsao(GmID)
        elif GmID == '53x1':
            XXD1(GmID)
        elif GmID == '53x2':
            XXD2(GmID)
        elif GmID == '51x':
            RO(GmID)
        else:
            print "游戏服务器码无效！"


## 主程序
if __name__ == '__main__':
    runJSON(GmID)