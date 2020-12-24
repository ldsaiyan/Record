# Tomcat弱口令&后台getshell漏洞

## 介绍
Tomcat支持在后台管理页面部署war文件，因此可以将webshell部署上去。访问后台管理页面一般是只允许本地ip访问或者需要输入账号密码访问的，对于后者，如果是弱口令，那么进入后台上传webshell指日可待。

## 版本以及准备
Tomcat/7.0.100
Windows7
JDK1.8

配置文件conf/tomcat-users.xml里面默认木有登录用户，那就自己添加一个

![](https://github.com/saiyanlee/Record/blob/master/Sys/Tomcat/Tomcat弱口令&后台getshell漏洞/images/1.png)

这样就能利用账号admin,密码admin进入管理应用界面

![](https://github.com/saiyanlee/Record/blob/master/Sys/Tomcat/Tomcat弱口令&后台getshell漏洞/images/2.png)

## 漏洞复现
访问http://192.168.0.100:8080/manager/html，输入admin:admin（有的弱口令是tomcat:tomcat），成功进入。

看到相关文章说版本在Tomcat 5.5.0 to 5.5.28或Tomcat 6.0.0 to 6.0.20之间，Tomcat默认会建立一个名为“admin”，密码为空的具有管理权限的账号。这也是猜解途径之一，另外就是看你的“字典”是否强大了

为了上传一个war格式的木马，先写一个JSP的一句话木马，压缩成.zip,再改后缀为.war

![](https://github.com/saiyanlee/Record/blob/master/Sys/Tomcat/Tomcat弱口令&后台getshell漏洞/images/3.png)

部署上去

![](https://github.com/saiyanlee/Record/blob/master/Sys/Tomcat/Tomcat弱口令&后台getshell漏洞/images/4.png)

![](https://github.com/saiyanlee/Record/blob/master/Sys/Tomcat/Tomcat弱口令&后台getshell漏洞/images/5.png)

上传成功

![](https://github.com/saiyanlee/Record/blob/master/Sys/Tomcat/Tomcat弱口令&后台getshell漏洞/images/6.png)

然后蚁剑连接就行

## 防范 
选择最新的稳定版本Tomcat，关注漏洞发布平台的最新Tomcat漏洞信息
Tomcat降权
增加密码强度
非必须的话可以删除该管理页面
等等