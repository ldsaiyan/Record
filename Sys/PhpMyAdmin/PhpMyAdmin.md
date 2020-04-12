## PhpMyadmin各版本漏洞合集

### 1.PhpMyAdmin存在PREGREPLACEEVAL漏洞
#### 影响版本：
3.5.x < 3.5.8.1 and 4.0.0 < 4.0.0-rc3
#### 利用模块：
exploit/multi/http/phpmyadminpregreplace
#### CVE:
CVE-2013-3238

### 2.PhpMyAdmin存在serversync.php 后门漏洞
#### 影响版本：
phpMyAdmin v3.5.2.2
#### 利用模块：
exploit/multi/http/phpmyadmin3522_backdoor
#### CVE:
CVE-2012-5159

### 3.PhpMyAdmin配置文件/config/config.inc.php存在命令执行
#### 影响版本：
2.11.x < 2.11.9.5 and 3.x < 3.1.3.1;
#### 利用模块：
exploit/unix/webapp/phpmyadmin_config
#### CVE:
CVE-2009-1151

### 4.通用密码漏洞
默认 phpMyAdmin：用户名 root、密码 root 或空登陆。


版本 2.11.3～2.11.4 、3.5.1：用户名 'localhost'@'@" 登陆，无需密码。


版本 2.11.9.2：用户名 root 登陆，无需密码。

### php爆绝对路径：
phpMyAdmin/libraries/selectlang.lib.php

phpMyAdmin/darkblueorange/layout.inc.php

phpMyAdmin/index.php?lang[]=1

phpmyadmin/themes/darkblue_orange/layout.inc.php


### 集合
seebug漏洞组件 — phpMyAdmin：
https://www.seebug.org/appdir/phpMyAdmin

## 来自
https://blog.csdn.net/abc_12366/article/details/83351049
https://www.cnblogs.com/M0rta1s/p/11517423.html