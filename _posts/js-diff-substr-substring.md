title: js中substring and slice和substr的用法区别
date: 2013-02-26 17:18:52
tags: JavaScript
categories: JavaScript
---

js的这2个截取字符语法很相近，容易混淆.

举例：

    var str = "0123456789";

    str.substr(0);---------------"0123456789" | "0123456789"----------str.substring(0);
    str.substr(5);---------------"56789"      | "56789"---------------str.substring(5);
    str.substr(10);--------------""           | ""--------------------str.substring(10);
    str.substr(12);--------------""           | ""--------------------str.substring(12);
    str.substr(-5);--------------"0123456789" | "0123456789"----------str.substring(-5);
    str.substr(0,5);-------------"01234"      | "01234"---------------str.substring(0,5);
    str.substr(2,0);-------------""           | "01"------------------str.substring(2,0);
    str.substr(2,2);-------------"23"         | ""--------------------str.substring(2,2);
    str.substr(2,5);-------------"23456"      | "234"-----------------str.substring(2,5);
    str.substr(2,12);------------"23456789"   | "23456789"------------str.substring(2,12);
    str.substr(2,-2);------------""           | "01"------------------str.substring(2,-2);
    str.substr(-1,5);------------"01234"      | "01234"---------------str.substring(-1,5);
    str.substr(-1,-5);-----------""           | ""--------------------str.substring(-1,-5);

<!-- more -->

## 说明:


* __substring__

   <code>substring</code> 方法返回的子串包括 <code>start</code> 处的字符，但不包括 <code>end</code> 处的字符。

   如果参数 <code>start</code> 与 <code>end</code> 相等，那么该方法返回的就是一个空串（即长度为 0 的字符串）。如果 <code>start</code> 比 <code>end</code> 大，那么该方法在提取子串之前会先 __交换__ 这两个参数。

   __重要事项__：与 <code>slice()</code> 和 <code>substr()</code> 方法不同的是，<code>substring()</code> 不接受负的参数。

* __slice__

   <code>slice()</code> 方法可提取字符串的某个部分，并以新的字符串返回被提取的部分。

   String 对象的方法 <code>slice()</code>、<code>substring()</code> 和 <code>substr()</code> （不建议使用）都可返回字符串的指定部分。<code>slice()</code> 比 <code>substring()</code> 要灵活一些，因为它允许使用负数作为参数。<code>slice()</code> 与 <code>substr()</code>有所不同，因为它用两个字符的位置来指定子串，而 <code>substr()</code> 则用字符位置和长度来指定子串。

   还要注意的是，<code>String.slice()</code> 与 <code>Array.slice()</code> 相似。

* __substr__ 

   如果 <code>start</code> 是负数且 <code>length</code> 小于等于 <code>start</code>，则 <code>length</code> 为 0。


   需要留意的用法:

       alert(str.substr(2,0));-------------""

       alert(str.substring(2,0));----------"01"


   【注】：应用substr和substring两个函数截取带有空格的字符串后的长度是每个空格算一个字符长度。例如：

        var a = "I am shi huan!"; a.substring(0, 5).length的值是5，而不是4，

        但alert(a.substring(0, 5));的值却是I am ，这样在做alert("I am" == a.substring(0, 5));的时

        候就是false了，alert("I am" == a.substring(0, 4));才是true。


 
## 总结：
    
> <code>substr</code>      end 位置指的是 __个数__

> <code>substring</code>   end 位置指的是 __位置__

> <code>slice</code>   end 位置指的是 __位置__ 并可以输入负数


*参考文献：*

   [w3c_substring](http://www.w3school.com.cn/js/jsref_substring.asp)

   [w3c_substr](http://www.w3school.com.cn/js/jsref_substr.asp)
