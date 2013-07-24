title: wamp 虚拟主机配置
date: 2013-06-23 12:17:54
tags: apache
categories: apache
---

{% include JB/setup %}


## 1. 配置apache的配置文件httpd.conf

寻找节点

    # Virtual hosts
    #Include conf/extra/httpd-vhosts.conf

有些配置可能是直接写出

    # Virtual hosts
    <VirtualHost *:80>
        ServerAdmin webmaster@dummy-host.example.com
        DocumentRoot "c:/Apache2/docs/dummy-host.example.com"
        ServerName dummy-host.example.com
        ServerAlias www.dummy-host.example.com
        ErrorLog "logs/dummy-host.example.com-error.log"
        CustomLog "logs/dummy-host.example.com-access.log" common
    </VirtualHost>

修改配置`conf/extra/httpd-vhosts.conf`

    <VirtualHost *:80>
        ServerName www.cyw.com
        DocumentRoot "D:\workspace\cyw"

        <Directory "D:\workspace\cyw">
            Options Indexes FollowSymLinks
            AllowOverride None
            Order allow,deny
            Allow from all
        </Directory>
    </VirtualHost>

## 2. 配置host文件

个人推荐写一个bat文件，来快速编辑hosts

    notepad "%SystemRoot%\system32\drivers\etc\hosts" 
    ipconfig /flushdns 
    exit

hosts添加需要网站

    127.0.0.1    www.cyw.com
    127.0.0.1    cyw.com

## 3. 重启apache

<abbr title="End of file">EOF</abbr>