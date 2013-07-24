title: PHP 环境配置
date: 2013-05-22 12:17:54
tags: PHP
categories: PHP
---

好吧，家里的虚拟机重装了Ubuntu，环境重新搭以下，记录下过程

## 1. 服务器 Nginx

在Ubuntu 安装 nginx 很轻松容易，ubuntu 12.10已经有了Nginx官方地址源

	## 安装
	sudo apt-get install nginx

	## 路径
	whereis nginx

	## 输出
	nginx: /usr/sbin/nginx /etc/nginx /usr/share/nginx /usr/share/man/man1/nginx.1.gz

	## 运行
	sudo /usr/sbin/nginx

	## 浏览器输入http://localhost/
	Welcome to nginx!

## 2. 安装 Mysql

	sudo apt-get install mysql-server

	sudo apt-get install mysql-client


## 3. 安装PHP5


	sudo apt-get install php5

	sudo apt-get install libapache2-mod-auth-mysql

	sudo apt-get install php5-mysql

所有的配置文件都在/etc/nginx下，并且每个虚拟主机已经安排在了/etc/nginx/sites-available下 

	vanilla@ubuntu:/etc/nginx/sites-available$ vim default 

	root : /usr/share/nginx/www

<!-- more -->

## 4. Redis

[Redis](http://atchen.com/blog/2013-01-30/ubuntu-install-redis2.2.13/)























<abbr title="End of file">EOF</abbr>