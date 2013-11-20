title: 富有想象力的input输入效果 - Fancy Input
date: 2013-02-27 11:22:40
tags: JQuery
categories: JavaScript
---

{% include JB/setup %}



当您输入文字的形式，这款jQuery插件提供的5个有趣的小动画。

如果您删除or输入coliss，看起来是这样的。

![gif演示图](http://i.imgur.com/3g9ulAS.gif)

* Link

    [Fancy Input - Demo - type something... ✌](http://dropthebit.com/demos/fancy_input/fancyInput.html)

    [Fancy Input - GitHub](https://github.com/yairEO/fancyInput)

<!-- more -->

## 浏览器支持

请访问火狐，Chrome，Safari浏览器，Opera在演示。对不起，IE只能进入像往常一样。

## Fancy Input 使用方法

实现是很简单的。

* Step 1: 

<link rel="stylesheet" href="fancyInput.css">
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
<script src='fancyInput.js'></script>

* Step 2: HTML

<div>
    <input type='text' />
</div>
<div>
    <textare></textarea>
</div>

* Step 3: JavaScript

<script>
    $('div :input').fancyInput();
</script>


via: [原文](http://coliss.com/articles/build-websites/operation/javascript/jquery-plugin-fancyinput.html)