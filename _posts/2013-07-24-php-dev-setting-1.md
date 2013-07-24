title: PHP 环境配置 - 续
date: 2013-06-05 12:17:54
tags: PHP
categories: PHP
---

{% include JB/setup %}


## 1. Memcache && Session

*1. 安装Memcache服务端*

	sudo apt-get install memcached

安装完Memcache服务端以后，我们需要启动该服务：

	memcached -d -m 128 -p 11211 -u root

	偷懒的可以打。。

	memcached -d

这里需要说明一下memcached服务的启动参数：

	-p 监听的端口 
	-l 连接的IP地址, 默认是本机 
	-d start 启动memcached服务 
	-d restart 重起memcached服务 
	-d stop|shutdown 关闭正在运行的memcached服务 
	-d install 安装memcached服务 
	-d uninstall 卸载memcached服务 
	-u 以的身份运行 (仅在以root运行的时候有效) 
	-m 最大内存使用，单位MB。默认64MB 
	-M 内存耗尽时返回错误，而不是删除项 
	-c 最大同时连接数，默认是1024 
	-f 块大小增长因子，默认是1.25
	-n 最小分配空间，key+value+flags默认是48 
	-h 显示帮助

*2. 安装Memcache客户端*

	sudo apt-get install php5-memcache

安装完以后我们需要在`php.ini`里进行简单的配置,打开`/etc/php5/fpm/php.ini`文件在末尾添加如下内容：


	[Memcache]

	; 一个高性能的分布式的内存对象缓存系统，通过在内存里维护一个统一的巨大的hash表，
	; 它能够用来存储各种格式的数据，包括图像、视频、文件以及数据库检索的结果等。

	; 是否在遇到错误时透明地向其他服务器进行故障转移。
	memcache.allow_failover = On

	; 接受和发送数据时最多尝试多少个服务器，只在打开memcache.allow_failover时有效。memcache.max_failover_attempts = 20

	; 数据将按照此值设定的块大小进行转移。此值越小所需的额外网络传输越多。
	; 如果发现无法解释的速度降低，可以尝试将此值增加到32768。
	memcache.chunk_size = 8192

	; 连接到memcached服务器时使用的默认TCP端口。
	memcache.default_port = 11211

	; 控制将key映射到server的策略。默认值”standard”表示使用先前版本的老hash策略。
	; 设为”consistent”可以允许在连接池中添加/删除服务器时不必重新计算key与server之间的映射关系。
	;memcache.hash_strategy = “standard”; 控制将key映射到server的散列函数。默认值”crc32″使用CRC32算法，而”fnv”则表示使用FNV-1a算法。
	; FNV-1a比CRC32速度稍低，但是散列效果更好。
	;memcache.hash_function = “crc32″


保存`php.ini`,执行`sudo service php5-fpm restart`重启PHP。
在PHP中使用`Memcache`

	<?php
	    $mem = new Memcache; //创建Memcache对象
	    $mem->connect(”127.0.0.1″, 11211); //连接Memcache服务器

	    $val = “这是一个Memcache的测试.”;
	    $key = md5($val);
	    $mem->set($key,  $val,  0,  120); //增加插入一条缓存，缓存时间为120s

	    if(($k = $mem->get(’key’))){ //判断是否获取到指定的key
	    echo ‘from cache:’.$k;
	    } else {
	    echo ‘normal’; //这里我们在实际使用中就需要替换成查询数据库并创建缓存.
	    }
	?>

<!-- more -->

对于key，通常用md5 查询语句来获取，在实际使用中根据具体需要来决定好了…
通过上面的步骤，我们就完成了`Memcache`的配置和基本使用…
`php5-memcache`扩展提供的方法


	Memcache::add — 添加一个值，如果已经存在，则返回false
	Memcache::addServer — 添加一个可供使用的服务器地址
	Memcache::close — 关闭一个Memcache对象
	Memcache::connect — 创建一个Memcache对象
	memcache_debug — 控制调试功能
	Memcache::decrement — 对保存的某个key中的值进行减法操作
	Memcache::delete — 删除一个key值
	Memcache::flush — 清除所有缓存的数据
	Memcache::get — 获取一个key值
	Memcache::getExtendedStats — 获取进程池中所有进程的运行系统统计
	Memcache::getServerStatus — 获取运行服务器的参数
	Memcache::getStats — 返回服务器的一些运行统计信息
	Memcache::getVersion — 返回运行的Memcache的版本信息
	Memcache::increment — 对保存的某个key中的值进行加法操作
	Memcache::pconnect — 创建一个Memcache的持久连接对象
	Memcache::replace — R对一个已有的key进行覆写操作
	Memcache::set — 添加一个值，如果已经存在，则覆写
	Memcache::setCompressThreshold — 对大于某一大小的数据进行压缩
	Memcache::setServerParams — 在运行时修改服务器的参数 

## Notice

在`php.ini`中 将`session.save_handler` 修改为`memcache`,并修改`save_path`指向`memcached`的地址和端口即可

	session.save_handler = memcache
	session.save_path = tcp://127.0.0.1:11211

Memcache的PECL这个扩展非常强大 可以支持failover以及分布存储 使用方法: 只需要在session.save_path的参数列表中 使用逗号分隔各个mcached服务器 则保存的session会经过hash之后保存到各个mc服务器中 而hash的算法.memcache支持两种,crc32以及fnv memcache.hash_function= {crc32,fnv} 文档中很少有提到fnv算法的,据说其散列要比crc32更好 但是我通过以下小小的程序实验之后,发现仍旧是crc32的散列算法分布的更加平均.

	ini_set("memcache.hash_function","crc32");
	$memcache = new Memcache;
	$memcache1 = new Memcache;
	$memcache2 = new Memcache;
	$memcache->addServer(‘localhost’, 11211);
	$memcache->addServer(‘localhost’, 11212);
	$memcache->flush();
	$memcache1->connect(‘localhost’,11211);
	$memcache2->connect(‘localhost’,11212);
	$fp1 = fopen(“mem1.txt”,”w”);
	$fp2 = fopen(“mem2.txt”,”w”);
	for($i=0;$i<1000;$i++){
		$memcache->set($i,$i,0,1000);
		fwrite($fp1,$memcache1->get($i).” “);
		fwrite($fp2,$memcache2->get($i).” “);
	}
	fclose($fp1);
	fclose($fp2);

接着我就session的保存进行了测试 我开了3个memcached进程进行测试

	ini_set("memcache.hash_function","fnv");
	ini_set("error_reporting","E_CORE_ERROR");
	$memcache1 = new Memcache;
	$memcache1->connect(‘localhost’,11211);
	$memcache1->flush();

	$memcache2 = new Memcache;
	$memcache2->connect(‘localhost’,11212);
	$memcache2->flush();

	$memcache3 = new Memcache;
	$memcache3->connect(‘localhost’,11213);
	$memcache3->flush();
	$fp1 = fopen(“mem1.txt”,”w”);
	$fp2 = fopen(“mem2.txt”,”w”);
	$fp3 = fopen(“mem3.txt”,”w”);
	for($i=0;$i<1000;$i++){
	session_start();
	$ssid=session_id();
	echo $ssid;
	session_register("id");
	$_SESSION["id"]=$ssid;
	session_write_close();
	fwrite($fp1,$memcache1->get($ssid).” “);
	fwrite($fp2,$memcache2->get($ssid).” “);
	fwrite($fp3,$memcache3->get($ssid).” “);
	//session_destroy();
	}
	fclose($fp1);
	fclose($fp2);
	fclose($fp3);

比较奇怪的是.memcached2一般都会不被选中 而1,3的内容是一致的.可能是为了failover 而当我把1,3关闭一台后.2中将会出现内容,说明memcached2是正常工作的 而不论我的散列算法使用crc32还是fnv 这种现象都存在 最后我发现.这个测试程序存在问题 因为在session_write_close之后.整个程序的session都是唯一的了. 也就是虽然循环了这么多次.里面包含了session_destroy调用.但是返回的session id都是同样的 这就导致了两个文件中的内容一致而另一个文件中没有内容 基于此点 我只能分次调用脚本,脚本修改如下


	ini_set("memcache.hash_strategy","consistent");
	ini_set("memcache.hash_function","crc32");
	ini_set("error_reporting","E_CORE_ERROR");
	ini_set("memcache.allow_failover","0");
	$memcache1 = new Memcache;
	$memcache1->connect(‘localhost’,10001);
	$memcache1->flush();

	$memcache2 = new Memcache;
	$memcache2->connect(‘localhost’,10002);
	$memcache2->flush();

	$memcache3 = new Memcache;
	$memcache3->connect(‘localhost’,10003);
	$memcache3->flush();
	$fp1 = fopen(“mem1.txt”,”a+”);
	$fp2 = fopen(“mem2.txt”,”a+”);
	$fp3 = fopen(“mem3.txt”,”a+”);
	session_start();
	$ssid=session_id();
	echo $ssid.”\n”;
	session_register(“id”);
	$_SESSION["id"]=$ssid;
	//session_destroy();
	session_write_close();
	fwrite($fp1,$memcache1->get($ssid).” “);
	fwrite($fp2,$memcache2->get($ssid).” “);
	fwrite($fp3,$memcache3->get($ssid).” “);
	session_destroy();
	fclose($fp1);
	fclose($fp2);
	fclose($fp3);

然后再shell中重复运行多次.返回的ID不同了 再打开mem*.txt文件查看 发现3个文件中,每个session会保存在其中两个文件.然后分布不同 这证明了使用memcache来保存session.一个是做到了failover.第二会按照session id来做hash分布保存
大家应该对Memcached的缓存性能都是有所赞赏的，因为他确实在缓存方面做的很是优秀，从而让也让成为我们的系统开发不可以缺少的一部分， 并且能够通过他的性能，让我们的应用程序无法从速度上还是性能上得到很大提升，今天我所要写的就是如果使用Memcached 来存放session ,因为我相信大家通过手册中可以看到有一个示例，我们和他们的相差不大，但为什么我要写出来呢？因为真正的让你在使用memcached存储 session的时候，确实会遇到很多困难的。比如你明明是设置了很多参数，但为什么通过session_id()却无法取得相应的存放的值 呢？？
下面是我所写的代码，大家可以试试，有哪些是必要的！

	ini_set('display_errors', 1);
	$host = 'localhost';
	$port = 11211;
	//$session_save_path = "tcp://$host:$port?persistent=1&weight=2&timeout=2&retry_interval=10,  ,tcp://$host:$port  ";
	$session_save_path = "tcp://".$host.":".$port;
	ini_set('session.save_handler', 'memcache');
	//ini_set('session.save_path', $session_save_path);
	ini_set('session.save_path', 'tcp://127.0.0.1:11211');
	session_start();
	if(!isset($_SESSION['Test'])) {
	    $_SESSION['Test'] = time();
	}
	$_SESSION['TEST3'] = time();
	print $_SESSION['Test'];
	echo "\r\n";
	print session_id();
	echo "\r\n";
	try {
	$memcache = new memcache();
	$memcache->connect($host, $port);
	$memcache->flush();
	}catch (Exception $e) {
	    $e->getTrace();
	}
	session_write_close();  //注意这个！，当你去掉后，你看下那个get值，是否能取出来！
	var_dump($_SESSION);
	var_dump($memcache);
	$id = session_id();
	var_dump($memcache->get($id));

ps: chmod 777|554 这东西不注意会让你无法访问

[参考使用memcached分布式保存PHP session](http://forum.z27315.com/topic/2295-%E4%BD%BF%E7%94%A8memcached%E5%88%86%E5%B8%83%E5%BC%8F%E4%BF%9D%E5%AD%98php-session/)


<abbr title="End of file">EOF</abbr>