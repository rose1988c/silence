title: problem-eclipse-jdk
date: 2013-05-09 22:32:00
tags: eclipse
categories: problem
---

{% include JB/setup %}


today, i download eclipse for helios, end of tar, when i open it.

shows 

	A Java RunTime Environment (JRE) or Java Development Kit (JDK) must be available in order to run Eclipse.No java virtual machine was found after searching the following locations:…

so angry.

do it :

	make sure you are install JDK


	解决办法是在终端进入你的eclipse目录，然后输入：

	mkdir jre
	cd jre

	ln -s 你的JDK目录/bin bin

<!-- more -->

附:ln 使用方法

ln是linux中又一个非常重要命令，它的功能是为某一个文件在另外一个位置建立一个同不的链接，这个命令最常用的参数是-s，具体用法是：ln –s 源文件 目标文件。
　　当我们需要在不同的目录，用到相同的文件时，我们不需要在每一个需要的目录下都放一个必须相同的文件，我们只要在某个固定的目录，放上该文件，然后在 其它的目录下用ln命令链接（link）它就可以，不必重复的占用磁盘空间。例如：ln –s /bin/less /usr/local/bin/less
　　-s 是代号（symbolic）的意思。
　　这里有两点要注意：第一，ln命令会保持每一处链接文件的同步性，也就是说，不论你改动了哪一处，其它的文件都会发生相同的变化；第二，ln的链接又 软链接和硬链接两种，软链接就是ln –s ** **，它只会在你选定的位置上生成一个文件的镜像，不会占用磁盘空间，硬链接ln ** **，没有参数-s， 它会在你选定的位置上生成一个和源文件大小相同的文件，无论是软链接还是硬链接，文件都保持同步变化。
　　如果你用ls察看一个目录时，发现有的文件后面有一个@的符号，那就是一个用ln命令生成的文件，用ls –l命令去察看，就可以看到显示的link的路径了。
　　指令详细说明
　　指令名称 : ln
　　使用权限 : 所有使用者
　　使用方式 : ln [options] source dist，其中 option 的格式为 :
　　[-bdfinsvF] [-S backup-suffix] [-V {numbered,existing,simple}]
　　[--help] [--version] [--]
　　说明 : Linux/Unix 档案系统中，有所谓的连结(link)，我们可以将其视为档案的别名，而连结又可分为两种 : 硬连结(hard link)与软连结(symbolic link)，硬连结的意思是一个档案可以有多个名称，而软连结的方式则是产生一个特殊的档案，该档案的内容是指向另一个档案的位置。硬连结是存在同一个档 案系统中，而软连结却可以跨越不同的档案系统。
　　ln source dist 是产生一个连结(dist)到 source，至于使用硬连结或软链结则由参数决定。
　　不论是硬连结或软链结都不会将原本的档案复制一份，只会占用非常少量的磁碟空间。
　　-f : 链结时先将与 dist 同档名的档案删除
　　-d : 允许系统管理者硬链结自己的目录
　　-i : 在删除与 dist 同档名的档案时先进行询问
　　-n : 在进行软连结时，将 dist 视为一般的档案
　　-s : 进行软链结(symbolic link)
　　-v : 在连结之前显示其档名
　　-b : 将在链结时会被覆写或删除的档案进行备份
　　-S SUFFIX : 将备份的档案都加上 SUFFIX 的字尾
　　-V METHOD : 指定备份的方式
　　--help : 显示辅助说明
　　--version : 显示版本
　　范例 :
　　将档案 yy 产生一个 symbolic link : zz
　　ln -s yy zz
　　将档案 yy 产生一个 hard link : zz
　　ln yy xx﻿


<abbr title="End of file">EOF</abbr>