title: PHP 面试题，上帝的愤怒
date: 2013-03-01 13:05:00
tags: PHP
categories: PHP
---

{% include JB/setup %}


看到一道很有意思的面试题目，叫上帝的愤怒，但无论上帝如何愤怒，我们终将浇灭他的怒火。


## 题目

我们碰到了大麻烦，一个新来的传教士惹恼了上帝，上帝很愤怒，要求我们把圣经（bbe.txt）背熟，直至他说哪个单词，我们就要飞快的回答出这个单词在第几行第几个单词位置。听说你是个优秀的程序员，那么髟助我们完成这个不可能的任务吧。
要求如下：
１）/myworks/example/bbe.txt，98版本英文圣经一本
２）输入部分要求如下：php ./example.php [单词]
３）输出部分如下：[单词] 1,2 2,4 5,6　表示：此单词在1行2列（第二个单词），2行4列…
说明：
１）此文本4MB之巨…
２）单词的含义：由英文字母（大小写），数字（0-9）组成的串
３）提供给你的机器OS为ubuntu 9.10，内存只有1G，而且，很不幸的，其中700M用来做了别的
４）上机考试不允许上网，但我装了man文档以及读取CHM以及PDF的阅读器，在电脑的桌面的CHM文件夹中，有相应的PHP参考手册
５）算法复杂度要求不能大于O（N^2）（就是N的平方）
６）什么？PHP低效且用起来不顺手，好的，你可以用别的语言来实现。但注意：提供给你的机器上只有python 2.4/perl 5.8/gcc[g++] 4.1

附 [bbe.txt (英文版圣经TXT)下载](http://ishare.iask.sina.com.cn/f/12042582.html)

<!-- more -->

## Code

__PHP__ 


    $word = 'gods';
    if($word == ''){
            echo "Please input a word\n";
            exit;
    }
    $fh = fopen('/home/cyw/tmp/bbe.txt', 'r') or exit("Unable to open file!");
    $line_number = 0;
    echo '[' . $word . '] ';
    while(!feof($fh)){
            $line = fgets($fh);
            $line_number++;
            echo search($word, $line, $line_number);
    }
    
    // 这个$line_number其实不用传入当参数的
    function search($word, $line, $line_number){
            $line = preg_split("/[\s,.:;']+/", $line);
            $keys = array_keys($line, $word);
            $pos = '';
            if($keys){
                    foreach($keys as $key){
                            $pos .= $line_number . ',' . ($key + 1) . ' ';
                    }
            }
            return $pos;
    }



__python__

    #--coding:utf-8-- 

    import sys 
    import re 

    filename = '/home/cyw/tmp/bbe.txt' 
    searchstr = raw_input('input :') 

    f = open(filename, 'r')

    num = 0
    total = 0

    while True:
            line = f.readline()
            string = re.search(searchstr, line)
            num += 1
            if string != None:
                    total += 1
                    print "行%d : %s，第%d次出现"%(num,line,total)
    f.close

    #结果不符合要求，我们需要修改下

    #--coding:utf-8-- 

    import sys 
    import re 

    filename = '/home/cyw/tmp/bbe.txt' 
    searchstr = raw_input('input :') 

    f = open(filename, 'r')

    num = 0
    total = 0

    print "[%s]"%(searchstr),

    while True:
            line = f.readline()

            string = re.search(searchstr,line)
            num += 1

            if string != None:
                    start = 0

                    while True:
                        index = line.find(searchstr, start)
                        # if search string not found, find() returns -1
                        # search is complete, break out of the while loop
                        if index == -1:
                            break
                        print( "%d,%d" % (num, index) ),
                        # move to next possible start p
                        start = index + 1
    f.close

    #虽然符合了要求，但单词判断有问题

    #--coding:utf-8-- 

    import sys 
    import re

    filename = '/home/cyw/tmp/bbe.txt' 
    searchstr = raw_input('input :') 

    f = open(filename, 'r')

    num = 0
    total = 0

    print "[%s]"%(searchstr),

    while True:
            line = f.readline()

            string = re.search(searchstr,line)
            num += 1

            if string != None:

            ##分割
                words = line.split(" ") #没有写好，这里需要再处理，获得单词
                for key,word in enumerate(words):
                if (searchstr == word):
                    print( "%d,%d" % (num, key) ),
        
    f.close

