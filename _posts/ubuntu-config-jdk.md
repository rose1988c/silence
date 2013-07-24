title: ubuntu-config-jdk
date: 2013-05-09 22:25:54
tags: Ubuntu
categories: Ubuntu
---


到[Oracle官网下在JDK](http://www.oracle.com/technetwork/java/javase/downloads/index.html)

下载了最新版jdk-xxx.tar.gz。
    
把下载的jdk-xxx.tar.gz移到安装目录，我直接放在／usr目录下。

切换到／usr目录

    cd /usr

解压jdk :

    sudo tar -zxvf jdk-xxx.tar.gz

OK,接下来配置环境变量：

    sudo gedit /etc/profile

在/etc/prifile文件后面添加(提示：这里JDK的路径改为你自己的安装路径):

    export JAVA_HOME=/usr/jdk-xxx
    export JRE_HOME=/usr/jdk-xxx/jre
    export PATH=$JAVA_HOME/bin:$JAVA_HOME/jre/bin:$PATH
    export CLASSPATH=$CLASSPATH:.:$JAVA_HOME/lib:$JAVA_HOME/jre/lib

使刚才修改的/etc/profile文件立刻生效

    . /etc/profile

<!-- more -->

修改系统默认JDK，并使之立马生效（提示：改为自己的路径哦, 如果要装myeclipse的话这一步是必须得，否则会出错哦）:

    sudo update-alternatives --install "/usr/bin/java" "java" "/usr/jdk-xxx/bin/java" 300
    sudo update-alternatives --install "/usr/bin/javac" "javac" "/usr/jdk-xxx/bin/javac" 300
    sudo update-alternatives --install "/usr/bin/javaws" "javaws" "/usr/jdk-xxx/bin/javaws" 300
    sudo update-alternatives --config java
    sudo update-alternatives --config javac
    sudo update-alternatives --config javaws

OK,操作完毕，用`java -version`查看效果，如果是刚才咱安装的那个`JDK`，就表示。。。你懂得！
    
Java运行命令小提示：

    java -jar *.jar //运行已经编译的.jar文件
    javac *.java    //编译.java文件
    javaws *.jnlp   //运行.jnlp文件


<abbr title="End of file">EOF</abbr>