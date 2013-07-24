title: PHP中不使用临时变量来交换两个数值变量？
date: 2013-02-04 14:20:07
tags: PHP
categories: PHP
---

## [题目] 如何在PHP中不使用临时变量来交换两个数值变量？

正常是交换两个变量的值应该使用中间变量：

{% codeblock PHP交换两个数值变量 lang:php %}

    function swap($a, $b){

      $temp = $a;

      $a = $b;

      $b = $temp;

    }

{% endcodeblock %}

<!-- more -->

## [解析]

* 这个方法很容易想到，但是只限于交换数值类型的变量：

{% codeblock swap - PHP交换两个数值变量 lang:php %}

    function swap (&$a,&$b){
        $a = $a+$b;
        $b = $a-$b;
        $a = $a-$b;
    }

{% endcodeblock %}

* 这方法是语言结构,想法很奇妙：

{% codeblock list - PHP交换两个数值变量 lang:php %}

    list($a, $b) = array($b, $a);
    list($user_id, $group_id) = explode('-', $string);//$string like (user_id - group_id);
    注：list — 把数组中的值赋给一些变量

{% endcodeblock %}


* 通过数组函数array_reverse


{% codeblock array_reverse - PHP交换两个数值变量 lang:php %}

    $arr=array($a,$b);
    $arr=array_reverse($arr);
    $a=$arr[0];

    $b=$arr[1];
    注：array_reverse — 返回一个单元顺序相反的数组

{% endcodeblock %}
 

* 直接使用数组操作：

{% codeblock array - PHP交换两个数值变量 lang:php %}

     $a = "aaa";
     $b = "bbb";

     $b = array($a, $b);

     $a = $b[1];
     $b = $b[0];

 {% endcodeblock %}