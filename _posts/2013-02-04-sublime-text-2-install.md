title: Ubuntu 安装 Sublime Text 2
date: 2013-02-01 14:35:20
tags: Sublime Text
categories: Ubuntu
---

{% include JB/setup %}



## 1. Add the PPA and install Sublime Text 2 in Ubuntu

    sudo add-apt-repository ppa:webupd8team/sublime-text-2  
    sudo apt-get update  

## 2. Install

    sudo apt-get install sublime-text-2-beta  
    or  
    sudo apt-get install sublime-text-2-dev

<!-- more -->

## 3. 右键菜单open with增加Sublime Text2

第二步安装了后会生成 <code>/usr/share/applications/sublime-text-2.desktop</code>

    sudo gedit ~/.local/share/applications/mimeapps.list

参考gedit增加一行

    text/plain=sublime-text-2.desktop;

## 4. 增加别名 

    gedit ~/.bashrc

增加以下：

    #Sublime Text 2
    alias sub='sublime-text-2'

## 5. 单独安装包下载
    
Site:[http://www.sublimetext.com/](http://www.sublimetext.com/)

Reprint:[http://songfantasy.iteye.com/blog/1536184](http://songfantasy.iteye.com/blog/1536184)
