# Administration Console 弱口令

## 介绍
JBoss的Administration Console管理页面

#### 环境搭建
使用docker部署JBoss

docker pull jboss/wildfly 镜像下来

实例一个容器，JBoss以单机模式开启
```
docker run -p 8080:8080 -p 9990:9990 -it jboss/wildfly /opt/jboss/wildfly/bin/standalone.sh -b 0.0.0.0 -bmanagement 0.0.0.0
```

访问页面，出现这样证明部署成功

![](https://github.com/saiyanlee/Record/blob/master/Sys/JBoss/Administration%20Console%20%E5%BC%B1%E5%8F%A3%E4%BB%A4/images/1.png)

随后进入Administration Console管理页面

![](https://github.com/saiyanlee/Record/blob/master/Sys/JBoss/Administration%20Console%20%E5%BC%B1%E5%8F%A3%E4%BB%A4/images/2.png)

提示要添加用户

然后进去到容器设置一下

![](https://github.com/saiyanlee/Record/blob/master/Sys/JBoss/Administration%20Console%20%E5%BC%B1%E5%8F%A3%E4%BB%A4/images/3.png)

再次访问，输入账号密码后成功进来Administration Console管理页面

![](https://github.com/saiyanlee/Record/blob/master/Sys/JBoss/Administration%20Console%20%E5%BC%B1%E5%8F%A3%E4%BB%A4/images/4.png)

#### 思路
然而访问这Administration Console管理页面往往会存在着弱口令，默认用户名和密码都是admin。不择手段进去之后就能进入管理页面里上传自己准备好的shell了

这里我只写了一个显示当前时间的jsp，并且放进shell.war里，等待部署。

![](https://github.com/saiyanlee/Record/blob/master/Sys/JBoss/Administration%20Console%20%E5%BC%B1%E5%8F%A3%E4%BB%A4/images/5.png)

上传我的shell.war

![](https://github.com/saiyanlee/Record/blob/master/Sys/JBoss/Administration%20Console%20%E5%BC%B1%E5%8F%A3%E4%BB%A4/images/6.png)

上传成功后就可以访问 http://your-ip:8080/your-war-name/your-jsp-name.jsp

我这里为 http://192.168.140.137:8080/shell/haha.jsp

![](https://github.com/saiyanlee/Record/blob/master/Sys/JBoss/Administration%20Console%20%E5%BC%B1%E5%8F%A3%E4%BB%A4/images/7.png)