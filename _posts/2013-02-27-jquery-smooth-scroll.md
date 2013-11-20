title: JQuery 实现锚链接之间的平滑滚动
date: 2013-02-27 15:20:37
tags: JQuery
categories: JavaScript
---

{% include JB/setup %}



* Step 1: 

<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>

* Step 2: HTML

<a href="javascript:void();" name="wantgo">想去wantgo的地方 - javascript:void();</a>

<a href="#wantgo" name="wantgo">想去wantgo的地方 - #wantgo</a>

<div id="wantgo" >
    I want go sky.
</div>

<!-- more -->

* Step 3: JavaScript

<script type="text/javascript">
    $(function() {

        //不用#控制的锚链接方法，推荐.为了优化jquery取得元素，可以在需要跳转的超链接加个单独样式
        $(".a").click(function(){
            var _name = $(this).attr("name");
            if ( _name.length > 2 ) {
                var $target = $("#" + _name);
                if ($target.length>0) {
                    var targetOffset = $target.offset().top;
                    $('html,body').animate({
                        scrollTop: targetOffset
                    },
                    500);
                    return false;
                }
            }
        });

        //用于#控制的超链接
        $('a[href*=#]').click(function() {
            if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
                var $target = $(this.hash);
                $target = $target.length && $target || $('[name=' + this.hash.slice(1) + ']');
                if ($target.length) {
                    var targetOffset = $target.offset().top;
                    $('html,body').animate({
                        scrollTop: targetOffset
                    },
                    1000);
                    return false;
                }
            }
        });

    });
</script>




















<!-- more -->