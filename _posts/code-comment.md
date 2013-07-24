---
title: 代码注释的优雅
date: 2013-01-24 11:12:56
categories: Diary
tags: Code
---

在[userscripts](http://userscripts.org)看到优雅的注释后，便诞生一个念头，如何写好注释，更加符合代码的优雅，于是便有了这文章

### 项目注释

描述一个项目

    // ------------------------------------------------------------------------
    // 
    // IMPORTANT NOTICE
    // The script does not and will not do automatic searches on the site it runs on, 
    // because it is very harmful to the site's performance. If you had the 
    // great idea of implementing such a feature you are STRONGLY advised not to do so.
    // OiNKPlus is not related to the supported sites in any way. Use at own risk.
    // Some functions were created by the Platypus extension.
    // The script may frequently break, therefore it will automatically check for updated 
    // versions every now and then.
    // The author does not claim the code to be elegant. 
    // Ok? Fine.
    // Suggestions, feedback and contributions welcome.
    //  

<!-- more -->

---

    // *** Powered by rgbcolor.js ***************************************
    /**
    * A class to parse color values
    * @author Stoyan Stefanov <sstoo@gmail.com>
    * @link   http://www.phpied.com/rgb-color-parser-in-javascript/
    * @license Use it if you like it
    */

---

    /*!
    * jQuery Cookie Plugin
    * https://github.com/carhartl/jquery-cookie
    *
    * Copyright 2011, Klaus Hartl
    * Dual licensed under the MIT or GPL Version 2 licenses.
    * http://www.opensource.org/licenses/mit-license.php
    * http://www.opensource.org/licenses/GPL-2.0
    */


### 块描述

每当你设置一个新功能或区分种类时，就可以在代码开始端加入块描述的注释方法。

    // ------------------------------------------------------------------------
    // Developed under Kubuntu Linux, Kate
    // ------------------------------------------------------------------------

---

    // === 設定の読み込み =================================
   
---

    // 2012.05.24 Auto_Domestic のバグ修正（過去の巡回しない原因はこれかも）
    //            自動内政のスキル追加（恵風・人選眼力・訓練系・修練系）
    //            市場情報をホスト名ごとに保存
    //            建設完了時間＞設定巡回時間 の時の巡回時間設定が間違ってたのを修正
    //            巡回時間にランダムで盛っていた秒を0秒～60秒から0秒～10秒に変更
    //            本拠地以外に市場があった場合に糧変換しなかったのを修正
    //            市場のある拠点が巡回対象以外でも糧変換するように修正
    //            内政スキル発動後に各処理が多分動作するように修正
    // 2012.05.25 拠点建設設定のデータがない拠点の初期データが間違っていたのを修正
    //            設定画面でNaN(Not a Number)が表示されていたのを修正
    // 2012.05.27 ビルスクの設定が反映されないのを修正

---

    /*
      Function: send
        Send a new message to all registered observers
        
      Parameters:
        sender    - Sender object (can be null)
        eventName - Event name (observers have to implement this method)
        options   - Object or Hash table (for multiple options) of sending event  (default null)
    */


### 类/群/声明的描述

我们经常可以在Javascript和CSS最上面看得到此类注释，往往都是说明该代码的出处，作者，联系方式，以及大致用途。

    /**
      * @desc opens a modal window to display a message
      * @param string $msg - the message to be displayed
      * @return bool - success or failure
    */

### 单行注释

程序代码重点部分加入注释，多而无用。

    // 色設定

    var COLOR_FRAME = "#333333";    // 枠背景色
    var COLOR_BASE  = "#654634";    // 拠点リンク色
    var COLOR_TITLE = "#FFCC00";    // 各BOXタイトル背景色
    var COLOR_BACK  = "#FFF2BB";    // 各BOX背景色

---

    //バグ回避 600000=5*60*1000
    // 領地画面や建築画面で停止した場合の処理
    // ５分間止まっていた場合拠点画面に移動する
    if(location.pathname == "/land.php" || location.pathname == "/facility/facility.php") {
        unsafeWindow.setTimeout(function(){location.href = "http://"+HOST+"/village.php";},300000);
    }
    // =============================================================================================
    //君主プロフィール画面なら都市画面URLを取得
    if ((location.pathname == "/user/" || location.pathname == "/user/index.php") &&
        getParameter("user_id") == "") {
        getUserProf(document);
        if ( getStayMode() ) {
            closeIniBilderBox()
            openIniBilderBox()
        }
    }


### 分割线

    //-----------------------------------TonDen---------------------------------

---

    // =========================================================================


### other

    // TODO:  等待实现的功能
    // FIXME: 需要修正的功能
    // XXX:   需要改进的功能

    // Magic. Do not touch.

    // drunk, fix later


