---
layout: post
title: 解除网页限制
categories : JavaScript
tags : [JavaScript]
comments : false
date: 2013-01-10 17:41:48
---

{% include JB/setup %}

复制/粘帖/不能选择/不能使用右键菜单

***

#### 方法一

{% codeblock Javascript lang:js http://blog.atchen.com %}
    (function() {
    eval(function(p, a, c, k, e, r) {
        e = function(c) {
            return (c < a ? '' : e(parseInt(c / a))) + ((c = c % a) > 35 ? String.fromCharCode(c + 29) : c.toString(36))
        };
        if (!''.replace(/^/, String)) {
            while (c--) r[e(c)] = k[c] || e(c);
            k = [function(e) {
                return %20r[e]
            }];
            e = function() {
                return '\\w+'
            };
            c = 1
        };
        while (c--) if (k[c]) p = p.replace(new % 20RegExp('\\b' + e(c) + '\\b', 'g'), k[c]);
        return %20p
    }('5%202=8;5%203=2.K;3.7=3.k=3.e=3.9=3.6=3.y=3.7=3.z=2.7=2.k=2.e=2.9=2.6=4;2.7=2.6=2.c=2.9=p(){r%20t};g(8.n||8){d=4;c=4;6=4}5%20a=8.15(\'*\');o(5%20i=a.q-1;i>=0;i--){5%20b=a[i];g(b.n||b){d=4;c=4}}s(h(\'%u%v%w%x%j%17%A%B%C%j%D\')+\'\\E\'+h(\'%F%G%H%I%J%l%L%l%M%N%O%P%Q%R%S%T%U%V%W%X%Y\')+\'\\Z.10.11\');3.m.13=\'14!f\';3.m.16=\'12!f\';', 62, 70, '||doc|bd|null|var|oncontextmenu|onselectstart|document|onkeydown|arAllElements|elmOne|onmousedown|onmouseup|onpaste|important|with|unescape||u5236|oncopy|u7528|style|wrappedJSObject|for|function|length|return|alert|true|u5DF2|u89E3|u9664|u590D|onmousemove|ondragstart|u53F3|u952E|u9650|uFF01|u000d|u66F4|u591A|u7CBE|u5F69|u5B9E|body|u5E94|uFF0C|u8BF7|u5173|u6CE8|u300E|u5F02|u6B21|u5143|u8F6F|u4EF6|u4E16|u754C|u300F|u000dwww|iPlaySoft|com|text|webkitUserSelect|auto|getElementsByTagName|MozUserSelect|u4E0E'.split('|'), 0, {}))
    })();
{% endcodeblock %}


#### 方法二
    setTimeout("document.oncontextmenu=null;document.ondragstart=null;document.onkeydown=null;document.onmousedown=null;document.onmousemove=null;document.onmouseup=null;document.onselectstart=null;document.body.oncontextmenu=null;document.body.ondragstart=null;document.body.onkeydown=null;document.body.onmousedown=null;document.body.onmousemove=null;document.body.onmouseup=null;document.body.onselectstart=null;window.oncontextmenu=null;window.ondragstart=null;window.onkeydown=null;window.onmousedown=null;window.onmousemove=null;window.onmouseup=null;window.onselectstart=null;window.onbeforeprint=null;",500);


#### Userscripts

使用方法:

  1.加入书签

  2.利用插件

<http://userscripts.org/scripts/show/155637> 


