title: PHP 汉语的正则
date: 2013-04-24 11:27:43
tags: PHP
categories: PHP 
---

{% include JB/setup %}


在编码GB2312 和 UTF-8 下，有所不同


    //GB2312汉字字母数字下划线正则表达式
    "/^[".chr(0xa1)."-".chr(0xff)."]+$/"

    //UTF-8汉字字母数字下划线正则表达式
    "/^[\x{4e00}-\x{9fa5}]+$/u"


js

    if (/^[\u4e00-\u9fa5]+$/.test(str)) {
        alert("该字符串全部是中文");
    } else {
        alert("该字符串不全部是中文");
    }


<abbr title="End of file">EOF</abbr>