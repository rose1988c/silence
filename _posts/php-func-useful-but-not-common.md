title: PHP 不常见却非常有用的函数
date: 2013-04-22 14:22:03
tags: PHP
categories: PHP
---

函数是PHP如此强大的源泉，但是很多PHP函数并没有得到充分的利用。这里，我们给大家简单介绍10个不常见，但非常有用的函数。

## 1. sys_getloadavg()

`sys_getloadavt()` 可以获得系统负载情况。
该函数返回一个包含三个元素的数组，每个元素分别代表系统再过去的1、5和15分钟内的平均负载。

与其让服务器因负 载过高而宕掉，不如在系统负载很高时主动die掉一个脚本，sys_getloadavg()就是用来帮你实现这个功能的。 不过很遗憾，该函数在windows下无效。

## 2. Pack()

`Pack()` 能将md5()返回的32位16进制字符串转换为16位的二进制字符串，可以节省存储空间。

## 3. cal_days_in_month()

`cal_days_in_month()`能够返回指定月份共有多少天。

<!-- more -->

## 4. _()

`WordPress`开发者经常能见到这个函数，还有 `_e()`。这两个函数功能相同，与`gettext()`函数结合使用，能实现网站的多语言化。具体可参见PHP手册的相关部分介绍。

## 5. get_browser()

在发送页面前先看看用户的浏览器都能做些什么是 不是挺好？`get_browser()`能获得用户的浏览器类型，以及浏览器支持的功能，不过首先你需要一个`php_browscap.ini`文件，用来给 函数做参考文件。

要注意，该函数对浏览器功能的判断是基于该类浏览器的一般特性的。

例如，如果用户关闭了浏览器对 `JavaScript`的支持，函数无法得知这一点。但是在判断浏览器类型和OS平台方面，该函数还是很准确的。

## 6. debug_print_backtrace()

这是一个调试用的函数，能帮助你发现代码中的逻辑错误。要理 解这个函数，还是直接看个例子吧：

    $a = 0;   
    function iterate() {   
        global $a;   
        if( $a < 10 )   
            recur();   
        echo $a . ", ";   
    }   
    function recur() {   
        global $a;   
        $a++;   
        // how did I get here?   
        echo "\n\n\n";   
        debug_print_backtrace();   
        if( $a < 10 )   
            iterate();   
    }   
    iterate();   

    # OUTPUT:   
    #0 recur() called at [C:\htdocs\php_stuff\index.php:8]   
    #1 iterate() called at [C:\htdocs\php_stuff\index.php:25]   
    #0 recur() called at [C:\htdocs\php_stuff\index.php:8]   
    #1 iterate() called at [C:\htdocs\php_stuff\index.php:21]   
    #2 recur() called at [C:\htdocs\php_stuff\index.php:8]   
    #3 iterate() called at [C:\htdocs\php_stuff\index.php:25]   
    #0 recur() called at [C:\htdocs\php_stuff\index.php:8]   
    #1 iterate() called at [C:\htdocs\php_stuff\index.php:21]   
    #2 recur() called at [C:\htdocs\php_stuff\index.php:8]   
    #3 iterate() called at [C:\htdocs\php_stuff\index.php:21]   
    #4 recur() called at [C:\htdocs\php_stuff\index.php:8]   
    #5 iterate() called at [C:\htdocs\php_stuff\index.php:25]  

## 7. metaphone()

这个函数返回单词的`metaphone`值，相同读音的单词具有相同的`metaphone`值，也就是说这个函数可以帮你判断两个单词的读音是否 相同。

## 8. natsort()

`natsort()`能将一个数组以自然排序法 进行排列，直接看个例子吧：

    $items = array(   
        "100 apples", "5 apples", "110 apples", "55 apples"   
    );   
    // normal sorting:   
    sort($items);   
    print_r($items);   
    
    # Outputs:   
    # Array   
    # (   
    # [0] => 100 apples   
    # [1] => 110 apples   
    # [2] => 5 apples   
    # [3] => 55 apples   
    # )   

    natsort($items);   
    print_r($items);   
    
    # Outputs:   
    # Array   
    # (   
    # [2] => 5 apples   
    # [3] => 55 apples   
    # [0] => 100 apples   
    # [1] => 110 apples   
    # )  

## 9. levenshtein()

`Levenshtein()`告诉你两个单词之间的"距离"。
它告诉你如果想把一个单词变成另一个单词，需要插入、替换和删除多少字母。

看个例子吧：

    $dictionary = array(   
        "php", "javascript", "css"   
    );   
    $word = "japhp";   
    $best_match = $dictionary[0];   
    $match_value = levenshtein($dictionary[0], $word);   
    foreach($dictionary as $w) {   
        $value = levenshtein($word, $w);   
        if( $value < $match_value ) {   
            $best_match = $w;   
            $match_value = $value;   
        }   
    }   
    echo "Did you mean the '$best_match' category?";  

## 10. glob()

`glob()`会让你觉得用 `opendir()`, `readdir()`和`closedir()`来寻找文件非常蠢。

    foreach (glob("*.php") as $file)   
    echo "$file\n"; 

<abbr title="End of file">EOF</abbr>