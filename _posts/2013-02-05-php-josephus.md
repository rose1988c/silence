---
layout: post
title: PHP - 约瑟夫环
date: 2013-02-04 14:54:35
tags: PHP
categories: PHP
---

{% include JB/setup %}


约瑟夫环是一个数学的应用问题：已知n个人（以编号1，2，3...n分别表示）围坐在一张圆桌周围。从编号为k的人开始报数，数到m的那个人出列；他的下一个人又从1开始报数，数到m的那个人又出列；依此规律重复下去，直到圆桌周围的人全部出列。

这个就是约瑟夫环问题的实际场景，有一种是要通过输入n,m,k三个正整数，来求出列的序列。

<!-- more --> 

## 数组方法


<?php
    //定义函数
    function get_josephus( $totals , $m , $current = 0){
        $number = count($totals);
        $num = 1;
        if(count($totals) == 1){
            echo '<font color="red">'.$totals[0].' Success!</font>';
            return;
        }else{
            while($num++ < $m){
                $current++ ; //现实生活中，以1开始
                $current = $current%$number;
            }
            echo "".$totals[$current]."Killed...<br/>";
            array_splice($totals , $current , 1);
            get_josephus($totals , $m , $current);//递归函数
        }
    }
    $n      = 13;           //总共数目
    $m      = 34;           //数到第几只的那被踢出去
    $totals = range(1, $n); //将编号1-$n放入数组中
    get_josephus($totals , $m);     //调用函数
？>


## 数学方法

问题描述：n个人（编号0~(n-1）），从0开始报数，报到m-1的退出，剩下的人继续从0开始报数。求胜利者的编号。
我们知道第一个人（编号一定是（m-1）%n) 出列之后，剩下的n-1个人组成了一个新的约瑟夫环

这里使用一个数学递推公式:

    f[i] = 0　　                  i = 1

    f[i] = (f[i-1] + m) % i 　　  i >= 2

解决方法:


     function get_josephus($n, $m) {        //$n为总数,$m为剔除步长
         $s = 0;                            //$s为success坐标,只有一只时,success坐标为0
         for($i = 2; $i <= $n; $i++) {      //依次向后递推,求到共有$n只,剔除步长为$m时的success坐标
             $s = ($s + $m) % $i;           //success坐标递推公式
         }
         return $s + 1;                     //现实生活中，以1开始
     }
     
     echo get_josephus(13, 34);

