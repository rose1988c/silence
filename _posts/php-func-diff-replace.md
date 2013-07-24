title: PHP 替换字符串函数strtr()和str_repalce()区别
date: 2013-03-15 14:20:34
tags: PHP
categories: PHP
---

## 定义和用法

* `strtr()`           函数转换字符串中特定的字符。

* `str_replace()`     函数使用一个字符串替换字符串中的另一些字符。


_语法_

    strtr(string,from,to) 或者 strtr(string,array)

    参数         描述
    string1     必需。规定要转换的字符串。
    from        必需（除非使用数组）。规定要改变的字符。
    to          必需（除非使用数组）。规定要改变为的字符。

    array       必需（除非使用 from 和 to）。一个数组，其中的键是原始字符，值是目标字符。

    --------------------------------------------------------------------------

    str_replace(find,replace,string,count)

    find        必需。规定要查找的值。
    replace     必需。规定替换 find 中的值的值。
    string      必需。规定被搜索的字符串。
    count       可选。一个变量，对替换数进行计数

<!-- more -->

## 区别

 
首先你要明白对应关系 - 相互对应的替换

    strtr("aidenliu","ai","b*cd") //b*denl*u
    ai
    b*cd

此函数是大小写敏感的,具如果发生多次替换，每一次替换的蓝本都是最原始的那个字符串，而不是在前一次替换的基础上替换，如

    strtr("aidenliu","aA","A@")  //会输出Aidenliu 而不是@idenliu

`strtr(string,array)` 为关联数组，用关联数组中的值替换原始字符串中出现的对应的键，如果发生多次替换，每次替换的对像都是最原始的那个字符串，而不是在一次替换的基础上替换（此点与`str_replace`不同）

    $table_change = array(
                            '='                   => '',
                            'description'         => '',
                            'content'             => '',
                            'content'             => '',
                            '"'                   => '',
    );
    $desc = strtr($m[0][0], $table_change);

`str_replace` 实例:

    多对一替换：想把内容字段里所有的<p></p>标签清除掉,替换成空 [@str_replace(array('<p>','</p>'), '', $Content)]

    一对一替换：想把内容字段里所有的<br>标签换成<p> [@str_replace('<br>', '<p>', $Content)]

    多对多替换：想把内容字段里的<br>换成<br />, 同时<p>换<hr>，把</p>全清除 [@str_replace(array('<br>', '<p>','</p>'), array('<br />','<hr>',''), $Content)]