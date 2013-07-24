title: js-argument-callee
date: 2013-04-22 13:48:57
tags: JavaScript
categories: JavaScript
---

{% include JB/setup %}


`arguments.callee` 表示引用当前正在执行的函数，或者说是调用arguments.callee的函数对象的引用，它给匿名函数提供了一种自我引用的方式

    var func = function() {
        alert(func === arguments.callee);
    }

    func();
　   
执行上述代码，可以看到alter出来的结果是true，注意，此处用的是“===”，就是说func与arguments.callee对象类型和值都相等。


上面讲了arguments.callee的定义，那么它用在什么场合呢？一般来说，它会和*匿名函数*一起结合来用。

<!-- more -->

例如js脚本当前等待页面某种条件是否满足，如果满足进行相应初始化处理，但不是一直等下去，超过一定时间就放弃等待

    var flag = false, start = (new Date()).getTime();
    //普通实现 1
        function fun1() {
        //flag状态会在其他地方修改，当满足条件后执行相应逻辑 
            if (flag) { 
                // do something 
                return;
            } 
            //超过等待时间，放弃 
            if ((new Date()).getTime() - start > 3000) {
                return;
            } 
            //等待一秒后重试 
            setTimeout(fun1, 1000);
        }

        fun1();

    //普通实现 2
        function fun2() {
            if (flag) {
            // do something
            clearInterval(handler);
            return;
            }
            if ((new Date()).getTime() - start > 3000) {
                clearInterval(handler);
                return;
            }
        }

        var handler = setInterval(func2, 1000);

    //匿名函数实现
        (function(){ 
            if (flag) { 
                // do something return;
            }
            if ((new Date()).getTime() - start > 3000) {
                return;
            }

            setTimeout(arguments.callee, 1000);
        })();

　　比如执行初始化操作，使用匿名函数的好处是确保只被执行一次，而前面两种实现，由于定义了函数，就有可能在别处被误调用，从而执行多次初始化。

　　再看一递归调用例子：求一个数的阶乘

    //普通实现
        function fun2(n) {
            if (n > 1) {
                return n * fun2(n -1);
            } 
            return 1;
        }
        var r1 = fun2(3);

    //使用匿名函数
        var r2 = (function(n) {
            if (n > 1) {
                return n * arguments.callee(n -1);
            }
            return 1;
        })(3);


一处时间循环调用代码，JS实现动态显示当前时间(12/24小时制)

    window.onload=function(){
        function nowTime(ev,type){
            /*
             * ev:显示时间的元素
             * type:时间显示模式.若传入12则为12小时制,不传入则为24小时制
             */
            //年月日时分秒
            var Y,M,D,W,H,I,S;
            //月日时分秒为单位时前面补零
            function fillZero(v){
                if(v<10){v='0'+v;}
                return v;
            }
            (function(){
                var d=new Date();
                var Week=['星期天','星期一','星期二','星期三','星期四','星期五','星期六'];
                Y=d.getFullYear();
                M=fillZero(d.getMonth()+1);
                D=fillZero(d.getDate());
                W=Week[d.getDay()];
                H=fillZero(d.getHours());
                I=fillZero(d.getMinutes());
                S=fillZero(d.getSeconds());
                //12小时制显示模式
                if(type && type==12){
                    //若要显示更多时间类型诸如中午凌晨可在下面添加判断
                    if(H<=12){
                        H='上午&nbsp;'+H;
                    }else if(H>12 && H<24){
                        H-=12;
                        H='下午&nbsp;'+fillZero(H);
                    }else if(H==24){
                        H='下午&nbsp;00';
                    }
                }
                ev.innerHTML=Y+'年'+M+'月'+D+'日 '+' '+W+'&nbsp;'+H+':'+I+':'+S;
                //每秒更新时间
                setTimeout(arguments.callee,1000);
            })();
        }
        
        //24小时制调用
        nowTime(document.getElementById('time24'));
        //12小时制调用
        nowTime(document.getElementById('time12'),12);

    }


<abbr title="End of file">EOF</abbr>