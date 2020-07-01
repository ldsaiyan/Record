## 漏洞介绍
NFS（Network File System）即网络文件系统，是FreeBSD支持的文件系统中的一种，它允许网络中的计算机之间通过TCP/IP网络资源共享。在NFS的应用中，本地NFS的客户端应用可以透明地读写位于远端NFS服务器上的文件，就像访问本地文件一样。



## 环境部署及复现前戏
靶机：Metasploitable2-Linux （IP：192.168.140.135）
攻击机：Kali （IP：192.168.140.131）

在Kali上用nmap对靶机进行默认扫描并且显示详细版本信息。
![](https://github.com/saiyanlee/Record/blob/master/Sys/CVE-2010-2075/images/1.png)

6667端口上运行着UnrealIRCd程序的irc服务。

## 漏洞复现
#### Metasploit
找到UnrealIRCd对应版本的exploit模块
![](https://github.com/saiyanlee/Record/blob/master/Sys/CVE-2010-2075/images/4.png)

调用该模块，设置必须的参数
![](https://github.com/saiyanlee/Record/blob/master/Sys/CVE-2010-2075/images/5.png)


设置攻击载荷，反弹shell
![](https://github.com/saiyanlee/Record/blob/master/Sys/CVE-2010-2075/images/7.png)

exploit，成功，本机4444端口就能操作啦
![](https://github.com/saiyanlee/Record/blob/master/Sys/CVE-2010-2075/images/8.png)
