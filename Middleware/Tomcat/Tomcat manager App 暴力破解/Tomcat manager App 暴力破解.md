# Tomcat manager App 暴力破解

#### 介绍
Tomcat后台管理页面，对于弱口令，存在暴力破解的风险。常见弱口令有 admin:admin tomcat:tomcat等

#### 复现
访问http://192.168.0.105:8080/manager/html,输入账户密码，抓包

![](https://github.com/saiyanlee/Record/blob/master/Sys/Tomcat/Tomcat%20manager%20App%20%E6%9A%B4%E5%8A%9B%E7%A0%B4%E8%A7%A3/images/1.png)

发送至Intruder模块进行爆破。

账号密码以 account:password 的方式并且用了Base64的编码趟在HTTP字段中的Authorization中。标记这个编码部分

![](https://github.com/saiyanlee/Record/blob/master/Sys/Tomcat/Tomcat%20manager%20App%20%E6%9A%B4%E5%8A%9B%E7%A0%B4%E8%A7%A3/images/2.png)

Payload type选择Custom iterator
自定义迭代器，设置三个positions（1是用户名；2是冒号；3是密码）

![](https://github.com/saiyanlee/Record/blob/master/Sys/Tomcat/Tomcat%20manager%20App%20%E6%9A%B4%E5%8A%9B%E7%A0%B4%E8%A7%A3/images/3.png)

在Payload Processing添加Base64-encode，还有取消Palyload Encoding的编码（这个url编码会干扰此处的爆破）

![](https://github.com/saiyanlee/Record/blob/master/Sys/Tomcat/Tomcat%20manager%20App%20%E6%9A%B4%E5%8A%9B%E7%A0%B4%E8%A7%A3/images/4.png)

开始爆破，爆破成功

![](https://github.com/saiyanlee/Record/blob/master/Sys/Tomcat/Tomcat%20manager%20App%20%E6%9A%B4%E5%8A%9B%E7%A0%B4%E8%A7%A3/images/5.png)

![](https://github.com/saiyanlee/Record/blob/master/Sys/Tomcat/Tomcat%20manager%20App%20%E6%9A%B4%E5%8A%9B%E7%A0%B4%E8%A7%A3/images/6.png)

#### 防范
增加密码强度
非必须的话可以删除该管理页面