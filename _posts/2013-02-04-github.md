---
layout: post
title: GigHub 安装与使用
categories : GitHub
tags : [GitHub]
date: 2013-01-11 17:41:48
---


## 1.安装程序
As Example With Ubuntu.

    sudo apt-get install git
    sudo apt-get install git-core


## 2.连接Github - SSH

生成 SSH 公钥

使用git服务器，需要生成一个ssh公钥,进入自己的~/.ssh目录，看有没有用 文件名 和 文件名.pub 来命名的一对文件，这个 文件名 通常是 id_dsa 或者 id_rsa。 

<!-- more -->

.pub 文件是公钥，另一个文件是密钥。假如没有这些文件（或者干脆连 .ssh 目录都没有），你可以用 ssh-keygen 的程序来建立它们，该程序在 Linux/Mac 系统由 SSH 包提供， 在 Windows 上则包含在 MSysGit 包里:

    ssh-keygen

它先要求你确认保存公钥的位置（.ssh/id_rsa），然后它会让你重复一个密码两次，如果不想在使用公钥的时候输入密码，可以留空。

现在，所有做过这一步的用户都得把它们的公钥给你或者 Git 服务器的管理者（假设 SSH 服务被设定为使用公钥机制）。他们只需要复制 .pub 文件的内容然后 e-email 之。

    cat ~/.ssh/id_rsa.pub 

个人觉得这部就好了，如果有更深层次的,[Ubuntu下修改SSH端口以及使用密匙登录](http://www.cnblogs.com/subsir/articles/2566114.html)

<!-- more -->

## 3.Clone or Create

Clone 一个存在的项目

    git clone git:xxx.git

Create 项目

    mkdir project
    cd project
    git init

这样，一个空的版本库就创建好了，并在当前目录中创建一个叫 .git 的子目录。

你可以用 ls -a 查看一下，并请注意其中的三项内容：
一个叫 **HEAD** 的文件，我们现在来查看一下它的内容:

    cat .git/HEAD

现在 HEAD 的内容应该是这样：

    ref: refs/heads/master

我们可以看到，HEAD 文件中的内容其实只是包含了一个索引信息，并且，这个索引将总是指向你的项目中的当前开发分支。

一个叫 **objects** 子目录，它包含了你的项目中的所有对象，我们不必直接地了解到这些对象内容，我们应该关心是存放在这些对象中的项目的数据。

一个叫 **refs** 的子目录，它用来保存指向对象的索引。

具体地说，子目录 refs 包含着两个子目录叫 heads 和 tags，就像他们的名字所表达的意味一样：他们存放了不同的开发分支的头的索引, 或者是你用来标定版本的标签的索引。

请注意：master 是默认的分支，这也是为什么 .git/HEAD 创建的时候就指向 master 的原因，尽管目前它其实并不存在。 git 将假设你会在 master 上开始并展开你以后的工作，除非你自己创建你自己的分支。

另外，这只是一个约定俗成的习惯而已，实际上你可以将你的工作分支叫任何名字，而不必在版本库中一定要有一个叫 master 的分支，尽管很多 git 工具都认为 master 分支是存在的。

现在已经创建好了一个 git 版本库，但是它是空的，还不能做任何事情，下一步就是怎么向版本库植入数据了。


## 4.植入内容跟踪信息：git add：

为了简明起见，我们创建两个文件作为练习：

    echo "Hello world" > hello
    echo "Silly example" > example

我们再用 git add 命令将这两个文件加入到版本库文件索引当中：

    git add hello example

git-add 实际上是个脚本命令，它是对 git 内核命令 git update-index 的调用。因此上面的命令和下面的命令其实是等价的：

    git add hello example
    git add .

如果你要将某个文件从 git 的目录跟踪系统中清除出去，同样可以用 git rm 命令。例如：

    git rm -rf xxx

git add 可以将某个目录下的所有内容全都纳入内容跟踪之下，例如： git add ./path/to/your/wanted 。但是在这样做之前，应该注意先将一些我们不希望跟踪的文件清理掉，例如，gcc 编译出来的 *.o 文件，vim 的交换文件 .*.swp 之类。

应该建立一个清晰的概念就是，git add 只是刷新了 git 的跟踪信息，hello 和 example 这两个文件中的内容并没有提交到 git 的内容跟踪范畴之内。


## 5.提交内容到版本库：git commit

　　既然我们刷新了 Git 的跟踪信息，现在我们看看版本库的状态：

    git status

我们能看到 git 的状态提示：

    #
    # Initial commit
    #
    #
    # Updated but not checked in:
    # (will commit)
    #
    # new file: example
    # new file: hello
    #

提示信息告诉我们版本库中加入了两个新的文件，并且 git 提示我们提交这些文件，我们可以通过 git-commit 命令来提交：

    git-commit -m "Initial commit of gittutor reposistory"


## 6.查看当前的工作：git diff

gitdiff 命令将比较当前的工作目录和版本库数据库中的差异。现在我们编辑一些文件来体验一下 git 的跟踪功能。

    echo "It's a new day for git" >> hello

我们再来比较一下，当前的工作目录和版本库中的数据的差别。

    git diff

差异将以典型的 patch 方式表示出来：

    diff --git a/hello b/hello
    index 802992c..8fdaa4e 100644
    --- a/hello
    +++ b/hello
    @@ -1 +1,2 @@
    Hello world
    +It's a new day for git


此时，我们可以再次使用组合命令 git-update-index 和 git-commit 将我们的工作提交到版本库中。

    git add hello
    git commit -m "new day for git"

实际上，如果要提交的文件都是已经纳入 git 版本库的文件，那么不必为这些文件都应用 git-update-index 命令之后再进行提交，下面的命令更简捷并且和上面的命令是等价的。

    git commit -a -m "new day for git"


## 7.提交
    
    git push origin master

## 一些命令：

初始化git数据库

    git init

添加文件

    git add hello.c

查看修改、提交记录

    git log

创建分支

    git branch roredu

查看分支

    git-branch
    * master
      roredu

切换工作分支

    git-checkout roredu
    Switched to branch "roredu"
    $ git-branch
    master
    * roredu

提交到当前工作分支并书写标记。

    git commit

创建xux分支对于master的补丁文件。

    git format-patch master roredu

配置开发者自己的签名和email。

    git config --global user.name "xxx"
    git config --global user.email "xxx@gmail.com"

修改文件名

    git mv roredu.c helight.c

删除文件

    git rm roredu.c

协同工作，下载项目：

    git clone ssh@wtb:192.168.0.21/home/wtb/NetBeansProjects/project1

这里wtb是用户名， 192.168.0.21是项目所在机器的IP 后面跟着的是项目目录和名称

放弃对file.cpp文件的修改，返回上次提交的代码。

    git checkout -- file.cpp


## git如何merge github forked repository里的代码更新?

Github里有个项目ruby-gmail，我需要从fork自同一个项目的另一个repository拿一些Bug Fix的代码

    link1：https://github.com/dcparker/ruby-gmail （原作者dcparker的repository）
    link2：https://github.com/jihao/ruby-gmail （我从link1 fork的repository）
    link3：https://github.com/geoffyoungs/ruby-gmail （geoffyoungs 从link1 fork的repository，然后他有些Bug修改，但是没被merge回原作者的link1的repository）  

也就我git clone repository到本地后，发现link3有我想要的代码，我要把link3上的改动merge到我的repository上，避免我花精力改相同的bug

git如何merge github forked repository里的更新?
具体做法是下面三步，以前没用git这么搞过，知道之后其实蛮简单

    git remote add geoffyoungs http://github.com/geoffyoungs/ruby-gmail.git
    git fetch geoffyoungs
    git merge geoffyoungs/master

本地的repository看上去是这样的：

    git remote -v
    geoffyoungs http://github.com/geoffyoungs/ruby-gmail.git (fetch)
    geoffyoungs http://github.com/geoffyoungs/ruby-gmail.git (push)
    origin http://jihao@github.com/jihao/ruby-gmail.git (fetch)
    origin http://jihao@github.com/jihao/ruby-gmail.git (push)

    git branch -a
    * master
    remotes/geoffyoungs/gh-pages
    remotes/geoffyoungs/master
    remotes/origin/HEAD -> origin/master
    remotes/origin/adimircolen-master
    remotes/origin/gh-pages
    remotes/origin/master


## Git错误non-fast-forward后的冲突解决 

1，强推，即利用强覆盖方式用你本地的代码替代git仓库内的内容

    git push -f

2，先把git的东西fetch到你本地然后merge后再push

    git fetch
    git merge

  这2句命令等价于

    $ git pull  

上面出现的 [branch "master"]是需要明确(.git/config)如下的内容
[branch "master"]
    remote = origin

    merge = refs/heads/master
这等于告诉git2件事:

1，当你处于master branch, 默认的remote就是origin。
2，当你在master branch上使用git pull时，没有指定remote和branch，那么git就会采用默认的remote（也就是origin）来merge在master branch上所有的改变

如果不想或者不会编辑config文件的话，可以在bush上输入如下命令行：

    $ git config branch.master.remote origin  
    $ git config branch.master.merge refs/heads/master  

之后再重新git pull下。

## 错误
    error: Untracked working tree file 'public/CNAME' would be overwritten by merge.  Aborting

    git clean -dqfx
    git pull

