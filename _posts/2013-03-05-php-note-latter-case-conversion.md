title: PHP 字母大小写转换总结
date: 2013-03-05 10:15:03
tags: PHP
categories: PHP
---

{% include JB/setup %}


* 将字符串转换成小写

<code>strtolower()</code> 该函数将传入的字符串参数所有的字符都转换成小写,并以小写形式放回这个字符串


* 将字符转成大写

<code>strtoupper()</code> 函数的作用同strtolower函数相反,是将传入的字符参数的字符全部转换成大写,并以大写的形式返回这个字符串.用法同strtolowe()一 样.

 
* 将字符串首字符转换成大写

<code>ucfirst()</code> 该函数的作用是将字符串的第一个字符改成大写,该函数返回首字符大写的字符串.

<code>lcfirst()</code> 第一个词首字母小写


* 将字符串每个单词的首字符转换成大写

<code>ucwords()</code> 该函数将传入的字符串的每个单词的首字符变成大写.如"hello world",经过该函数处理后,将返回"Hello Word"


<!-- more -->


## 把字符串转中的_a_换为大写。

     $needreplace = 'a';
     $strs = array(
                    'hello atchen',
                    'good afternoon',
                    'thinks at night'
     );
     
     foreach ($strs as $k => $str) {
         
         $chars = str_split($str);
         
         foreach ($chars as $key => $char) {
             if (strcmp($char, $needreplace) == 0) { // or $char !== $needreplace
                 $chars[$key] = strtoupper($char);
             }
         }
         
         $strs[$k] = implode('', $chars);
     }


     //Out Put
     Array
     (
        [0] => hello Atchen
        [1] => good Afternoon
        [2] => thinks At night
     )














