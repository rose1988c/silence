title: PHP - Trim() 函数巧妙去掉字符
date: 2013-02-04 12:14:41
tags: PHP
categories: PHP
---

{% include JB/setup %}


昨天小阙问我，去取字符串尾部字符的几种方式?我说了以下几种方式

* <code>substr(string,start,length)</code>
* <code>str_replace(find,replace,string,count)</code>
* <code>explode() 函数把字符串分割为数组。循环替换</code>

后来我知道，原来<code>trim()</code>函数也能做到

## 定义和用法

<code>trim()</code> 函数从字符串的两端删除空白字符和其他预定义字符。

语法

    trim(string,charlist)

    参数         描述
    string      必需。规定要检查的字符串。
    charlist    可选。规定要转换的字符串。如果省略该参数，则删除以下所有字符：
                "\0" - NULL
                "\t" - tab
                "\n" - new line
                "\x0B" - 纵向列表符
                "\r" - 回车
                " " - 普通空白字符

从它的定义就能看出来，它不仅仅只用于去取空格,还可以去取特定字符

兄弟函数:

    ltrim() && rtrim()

<!-- more -->

用法:

{% codeblock PHP去除字符串中的最后一个字符 lang:php %}
    
    $str="aaaa,bbb,ccc,ddd,eee,";

    //第一种方法 trim($str,$chsrlist)去除两边的
    echo rtrim($str,','); 

    //第二种方法
    echo substr($str,0,strlen($str)-1); 

    //第三种方法
    echo substr($str,0,-1); 

    //第四种方法
    echo $str{strlen($str)-1} == ',' ? substr($str, 0, -1) : $str; 

{% endcodeblock %}


我觉得使用<code>rtrim()</code>函数还是比较好的,推荐使用！

如去除右边的逗号：

    $new_str = rtrim( trim($str), ',' );

去除多个字符：

    $new_str = rtrim( trim($str),',.;' );


## End

关注PHP，更应关注函数的选填参数，提高自己的编码水平.

上面出现的函数:

{% codeblock PHP函数的选填参数 lang:php %}
    
    /*
        string  必需。规定要返回其中一部分的字符串。
        start   必需。规定在字符串的何处开始。
                正数 - 在字符串的指定位置开始
                负数 - 在从字符串结尾的指定位置开始
                0 - 在字符串中的第一个字符处开始
        length  可选。规定要返回的字符串长度。默认是直到字符串的结尾。
                正数 - 从 start 参数所在的位置返回
                负数 - 从字符串末端返回
     */
    substr(string,start,length);

    /*
        find        必需。规定要查找的值。
        replace     必需。规定替换 find 中的值的值。
        string      必需。规定被搜索的字符串。*可以是数组哦。*
        count       可选。一个变量，对替换数进行计数。
     */
    str_replace(find,replace,string,count);

    /*
        separator   必需。规定在哪里分割字符串。
        string      必需。要分割的字符串。
        limit       可选。规定所返回的数组元素的最大数目。
     */
    explode(separator,string,limit)
{% endcodeblock %}