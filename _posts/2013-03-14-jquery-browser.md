title: jQuery 1.9 移除了 $.browser 的替代方法
date: 2013-03-14 14:26:09
tags: JQuery
categories: JavaScript
---

{% include JB/setup %}


jQuery 从 1.9 版开始，移除了 `$.browser` 和 `$.browser.version` ， 取而代之的是 `$.support` 。 在更新的 2.0 版本中，将不再支持 IE 6/7/8。 以后，如果用户需要支持 IE 6/7/8，只能使用 jQuery 1.9。 如果要全面支持 IE，并混合使用 jQuery 1.9 和 2.0， 官方的解决方案是：

    <!--[if lt IE 9]>
        <script src='jquery-1.9.0.js'></script>
    <![endif]-->
    <!--[if gte IE 9]>
        <script src='jquery-2.0.0.js'></script>
    <![endif]-->

从长久来看，这样有利于在复杂情况下根据浏览器特性进行分别处理， 而不是简单的检测浏览器类型和版本。 但目前很多旧程序的移植恐怕无法直接过渡为根据浏览器支持特性

<!-- more -->

## 判断本质

    var userAgent = navigator.userAgent.toLowerCase();

    // Figure out what browser is being used
    jQuery.browser = {
        version: (userAgent.match( /.+(?:rv|it|ra|ie)[\/: ]([\d.]+)/ ) || [])[1],
        safari: /webkit/.test( userAgent ),
        opera: /opera/.test( userAgent ),
        msie: /msie/.test( userAgent ) && !/opera/.test( userAgent ),
        mozilla: /mozilla/.test(userAgent)&&!/(compatible|webkit)/.test(userAgent)
    };


在1.4.2版本进化为
    
        ....

        uaMatch: function( ua ) {
            ua = ua.toLowerCase();

            var match = 
                /(webkit)[ \/]([\w.]+)/.exec( ua ) ||
                /(opera)(?:.*version)?[ \/]([\w.]+)/.exec( ua ) ||
                /(msie) ([\w.]+)/.exec( ua ) ||
                !/compatible/.test( ua ) && /(mozilla)(?:.*? rv:([\w.]+))?/.exec( ua ) ||
                [];

            return { browser: match[1] || "", version: match[2] || "0" };
        },

        browser: {}
    });

    browserMatch = jQuery.uaMatch( navigator.userAgent );
    if ( browserMatch.browser ) {
        jQuery.browser[ browserMatch.browser ] = true;
        jQuery.browser.version = browserMatch.version;
    }

    // Deprecated, use jQuery.browser.webkit instead
    if ( jQuery.browser.webkit ) {
        jQuery.browser.safari = true;
    }


补上上面的代码，弥补ie6-7-8的判断













