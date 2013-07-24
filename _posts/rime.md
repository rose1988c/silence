title: Rime - 小狼毫输入法
date: 2013-02-01 21:19:38
tags: Rime
categories: Interesting Software
---

小狼毫是基于Rime的输入法，Rime的中文名中州韻輸入法引擎，在各个平台上都有不同的实现。

在Windows下叫做小狼毫。Ubuntu下叫中州韵，Mac下叫鼠须管，不知道为什么叫的这么复杂。真是汗。

## 配置目录

* Windows下是 <code>%APPDATA%\Rime</code>，也可以在任务栏图标里面右键-用户文件夹

* Mac下是 <code>~/Library/Rime</code>，也可以在任务栏图标里面右键-Settings

<!-- more -->

# 输入习惯修改

## 1. 去掉F4快捷键（F4很多冲突）

打开安装路径文件夹的 <code>\data\default.yaml</code>

比如我的 <code>C:\Program Files\Rime\weasel-0.9.18\data\default.yaml</code>

去掉  <code>hotkeys:</code> 下的 F4一行

可能保存不了，可以先复制到外面 ，然后，修改后再复制回来

<code>%APPDATA%\Rime</code> 里面的 <code>default.yaml</code> 也需要同样修改。


**为什么要修改2处？**

安装路径文件夹是基础配置文件，<code>%APPDATA%\Rime</code>是用户配置。

如果仅仅修改用户配置，切换皮肤或者输入法的时候将会覆盖，导致失效。如果你仅仅修改基础配置文件是可以的，不过需要重新点击exe文件进行初始化用户配置，随便点个输入法，必须有改动才能设置。


## 2. 设置横排

同目录下 <code>weasel.yaml</code>

<code>horizontal: false</code>

搞成ture

<code>horizontal: true</code>

<code>%APPDATA%\Rime</code> 修改 <code>weasel.yaml</code>

貌似现在新版默认横排了。


## 3. 双拼模糊拼音

这个文件，将以下内容附到后面即可，保持speller/algebra和上面的switch对齐：

<code>double_pinyin_mspy.custom.yaml</code>

	"speller/algebra":
    - erase/^xx$/
    - derive/^([zcs])h/$1/ 
       - derive/^([zcs])([^h])/$1h$2/ 
       - derive/^n/l/ 
       - derive/^l/n/ 
       - derive/^([bpmf])eng$/$1ong/ 
       - derive/([ei])n$/$1ng/ 
       - derive/([ei])ng$/$1n/ 
    - derive/^([jqxy])u$/$1v/
    - derive/^([aoe].*)$/o$1/
    - xform/^([ae])(.*)$/$1$1$2/
    - xform/iu$/Q/
    - xform/[iu]a$/W/
    - xform/er$|[uv]an$/R/
    - xform/[uv]e$/T/
    - xform/v$|uai$/Y/
    - xform/^sh/U/
    - xform/^ch/I/
    - xform/^zh/V/
    - xform/uo$/O/
    - xform/[uv]n$/P/
    - xform/i?ong$/S/
    - xform/[iu]ang$/D/
    - xform/(.)en$/$1F/
    - xform/(.)eng$/$1G/
    - xform/(.)ang$/$1H/
    - xform/ian$/M/
    - xform/(.)an$/$1J/
    - xform/iao$/C/
    - xform/(.)ao$/$1K/
    - xform/(.)ai$/$1L/
    - xform/(.)ei$/$1Z/
    - xform/ie$/X/
    - xform/ui$/V/
    - derive/T$/V/
    - xform/(.)ou$/$1B/
    - xform/in$/N/
    - xform/ing$/;/
    - xlit/QWRTYUIOPSDFGHMJCKLZXVBN/qwrtyuiopsdfghmjcklzxvbn/


## 4. 扩充

朙月拼音詞典（擴充），可用來替換安裝目錄下的 <code>luna_pinyin.dict.yaml</code>

[下载地址](https://code.google.com/p/rime-aca/downloads/detail?name=luna_pinyin.dict.yaml)


## 5. 候选项

<code>default.yaml</code>

	menu:
		page_size: 8


## 6. Caps Lock 大小写键设置

<code>default.custom.yaml</code>

* 不切换，大小写反转

  patch: {
    ascii_composer/switch_key/Caps_Lock: noop
  }

* Caps Lock 灯亮，输出字母，以Shift变换大小写；这种方式与 Mac 系统默认输入法的行为一致，故默认采用这项设置
	
  patch: {
  	ascii_composer/switch_key/Caps_Lock: commit_code
  }

* Caps Lock 灯亮，只输出大写字母 - 习惯的方式 Window 方式 **推荐**

	patch: {
		ascii_composer/switch_key/Caps_Lock: commit_code
		ascii_composer/good_old_caps_lock: true
	}


## 结尾

  优点：速度很快、呼出切换很流畅、尽管折腾

  缺点：聚焦需改进

  以上操作需要重新设置，就是打开\weasel-0.9.18\WeaselDeployer.exe 选个不一样的选项，进行重新保存设置。如果一致是不保存的。